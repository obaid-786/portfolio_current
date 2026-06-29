/* =========================================================
   Front-end interactions:
   - Loading screen
   - Theme toggle (persisted in localStorage)
   - Typing effect
   - Scroll progress + scroll-to-top
   - Reveal-on-scroll
   - Animated counters
   - Active nav highlighting
   - Mobile menu
   - Project filtering
   - Contact form (AJAX to FastAPI)
   - Particle background
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {
  // ---- Render Lucide icons ----
  if (window.lucide) lucide.createIcons();

  // ---- Loading screen ----
  const loader = document.getElementById("loader");
  window.addEventListener("load", () => {
    setTimeout(() => loader && loader.classList.add("opacity-0", "pointer-events-none"), 400);
    setTimeout(() => loader && (loader.style.display = "none"), 900);
  });

  // ---- Theme toggle (default = system preference, persisted) ----
  const root = document.documentElement;
  const storedTheme = localStorage.getItem("theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  if (storedTheme === "dark" || (!storedTheme && prefersDark)) root.classList.add("dark");

  const themeToggle = document.getElementById("theme-toggle");
  themeToggle?.addEventListener("click", () => {
    root.classList.toggle("dark");
    localStorage.setItem("theme", root.classList.contains("dark") ? "dark" : "light");
  });

  // ---- Footer year ----
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // ---- Typing effect ----
  const typingEl = document.getElementById("typing");
  const roles = [
    "Software Developer", "FastAPI Developer", "AI Engineer",
    "IoT Developer", "ML Enthusiast",
  ];
  let roleIndex = 0, charIndex = 0, deleting = false;
  function type() {
    if (!typingEl) return;
    const current = roles[roleIndex];
    typingEl.textContent = current.substring(0, charIndex);
    if (!deleting && charIndex < current.length) {
      charIndex++; setTimeout(type, 90);
    } else if (deleting && charIndex > 0) {
      charIndex--; setTimeout(type, 45);
    } else {
      if (!deleting) { deleting = true; setTimeout(type, 1400); }
      else { deleting = false; roleIndex = (roleIndex + 1) % roles.length; setTimeout(type, 300); }
    }
  }
  type();

  // ---- Scroll progress bar ----
  const progress = document.getElementById("scroll-progress");
  const scrollTopBtn = document.getElementById("scroll-top");
  const navbar = document.getElementById("navbar");
  window.addEventListener("scroll", () => {
    const scrollTop = window.scrollY;
    const height = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) progress.style.width = `${(scrollTop / height) * 100}%`;

    // Show scroll-to-top after 400px.
    if (scrollTopBtn) {
      scrollTopBtn.classList.toggle("hidden", scrollTop < 400);
      scrollTopBtn.classList.toggle("flex", scrollTop >= 400);
    }
    // Navbar shadow when scrolled.
    navbar?.classList.toggle("scrolled", scrollTop > 20);

    highlightNav();
  });

  scrollTopBtn?.addEventListener("click", () =>
    window.scrollTo({ top: 0, behavior: "smooth" })
  );

  // ---- Reveal on scroll (IntersectionObserver) ----
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );
  document.querySelectorAll(".reveal").forEach((el) => revealObserver.observe(el));

  // ---- Animated counters ----
  const counterObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const target = +el.dataset.target;
        let count = 0;
        const step = Math.max(1, Math.ceil(target / 60));
        const tick = () => {
          count += step;
          if (count >= target) { el.textContent = target; }
          else { el.textContent = count; requestAnimationFrame(tick); }
        };
        tick();
        counterObserver.unobserve(el);
      });
    },
    { threshold: 0.5 }
  );
  document.querySelectorAll(".counter").forEach((el) => counterObserver.observe(el));

  // ---- Active nav highlighting ----
  const sections = document.querySelectorAll("section[id]");
  function highlightNav() {
    const scrollPos = window.scrollY + 120;
    sections.forEach((sec) => {
      const link = document.querySelector(`.nav-link[href="#${sec.id}"]`);
      if (!link) return;
      if (scrollPos >= sec.offsetTop && scrollPos < sec.offsetTop + sec.offsetHeight) {
        document.querySelectorAll(".nav-link").forEach((l) => l.classList.remove("active"));
        link.classList.add("active");
      }
    });
  }

  // ---- Mobile menu ----
  const menuBtn = document.getElementById("menu-btn");
  const mobileMenu = document.getElementById("mobile-menu");
  menuBtn?.addEventListener("click", () => mobileMenu.classList.toggle("hidden"));
  document.querySelectorAll(".mobile-link").forEach((link) =>
    link.addEventListener("click", () => mobileMenu.classList.add("hidden"))
  );

  // ---- Project filtering ----
  const filterBtns = document.querySelectorAll(".filter-btn");
  const projectCards = document.querySelectorAll(".project-card");
  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const filter = btn.dataset.filter;
      // Update active button styling.
      filterBtns.forEach((b) => {
        b.classList.remove("bg-brand", "text-white");
        b.classList.add("glass");
      });
      btn.classList.add("bg-brand", "text-white");
      btn.classList.remove("glass");
      // Show/hide cards.
      projectCards.forEach((card) => {
        const match = filter === "all" || card.dataset.category === filter;
        card.style.display = match ? "flex" : "none";
      });
    });
  });

  // ---- Contact form submission (AJAX) ----
  const form = document.getElementById("contact-form");
  const status = document.getElementById("form-status");
  const submitBtn = document.getElementById("submit-btn");
  form?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const payload = {
      name: form.name.value.trim(),
      email: form.email.value.trim(),
      subject: form.subject.value.trim(),
      message: form.message.value.trim(),
    };
    submitBtn.disabled = true;
    submitBtn.classList.add("opacity-60");
    showStatus("Sending…", "text-slate-500");

    try {
      const res = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await res.json();
      if (res.ok && data.success) {
        showStatus(data.message, "text-green-500");
        form.reset();
      } else {
        showStatus(data.message || "Failed to send. Try again.", "text-red-500");
      }
    } catch (err) {
      showStatus("Network error. Please try again.", "text-red-500");
    } finally {
      submitBtn.disabled = false;
      submitBtn.classList.remove("opacity-60");
    }
  });

  function showStatus(msg, colorClass) {
    if (!status) return;
    status.textContent = msg;
    status.className = `text-sm text-center ${colorClass}`;
    status.classList.remove("hidden");
  }

  // ---- Particle background ----
  initParticles();
});

/* ---------------------------------------------------------
   Lightweight canvas particle background.
   Subtle floating dots connected by lines near the cursor.
   --------------------------------------------------------- */
function initParticles() {
  const canvas = document.getElementById("bg-particles");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  let particles = [];
  const COUNT = window.innerWidth < 768 ? 30 : 60;

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener("resize", resize);

  // Initialize particles with random position/velocity.
  for (let i = 0; i < COUNT; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.4,
      vy: (Math.random() - 0.5) * 0.4,
      r: Math.random() * 2 + 1,
    });
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const isDark = document.documentElement.classList.contains("dark");
    const dotColor = isDark ? "rgba(99,102,241,0.6)" : "rgba(99,102,241,0.4)";

    particles.forEach((p) => {
      p.x += p.vx; p.y += p.vy;
      // Bounce off edges.
      if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
      if (p.y < 0 || p.y > canvas.height) p.vy *= -1;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = dotColor;
      ctx.fill();
    });

    // Connect nearby particles with faint lines.
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.hypot(dx, dy);
        if (dist < 120) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = isDark
            ? `rgba(99,102,241,${0.15 * (1 - dist / 120)})`
            : `rgba(99,102,241,${0.1 * (1 - dist / 120)})`;
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(draw);
  }
  draw();
}
