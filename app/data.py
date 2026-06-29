"""
Portfolio content data.

Centralizes all the site's textual content so templates remain clean and
content edits live in one place. This is rendered server-side by Jinja2.
"""

# --- Hero ---
HERO = {
    "name": "Obaidullah Siddiqui",
    "title": "Software Developer | Backend Developer | AI & IoT Enthusiast",
    "intro": (
        "Passionate Software Developer with hands-on experience in Backend "
        "Development, IoT Systems, Artificial Intelligence, and modern web "
        "technologies. Proven ability to design, develop, and deploy scalable "
        "solutions in both team and independent environments. Dedicated to "
        "building innovative software solutions that solve real-world problems."
    ),
    # Strings cycled through by the typing animation.
    "typing_roles": [
        "Software Developer",
        "FastAPI Developer",
        "AI Engineer",
        "IoT Developer",
        "ML Enthusiast",
    ],
}

# --- About ---
ABOUT = {
    "text": (
        "Passionate and results-driven Software Developer with expertise in "
        "Python, FastAPI, Machine Learning, IoT, and Full Stack Development. "
        "Experienced in building scalable applications, AI-powered systems, and "
        "real-time IoT solutions. Adept at problem-solving, software "
        "architecture, and delivering high-quality products."
    ),
    "stats": [
        {"value": 4, "suffix": "+", "label": "Major Projects"},
        {"value": 2, "suffix": "", "label": "High-Profile IoT Systems"},
        {"value": 97, "suffix": "%", "label": "ML Accuracy"},
        {"value": 0, "suffix": "", "label": "B.Tech IT (2022–2026)", "is_text": True,
         "text": "B.Tech IT"},
    ],
}

# --- Skills (grouped categories) ---
SKILLS = [
    {"category": "Languages", "icon": "code-2",
     "items": ["Python", "JavaScript", "Java"]},
    {"category": "Frontend Development", "icon": "layout",
     "items": ["React", "HTML", "CSS"]},
    {"category": "Backend Development", "icon": "server",
     "items": ["FastAPI", "Node.js (Basic)"]},
    {"category": "Databases & Tools", "icon": "database",
     "items": ["SQL", "Git"]},
    {"category": "Concepts & Methodologies", "icon": "git-branch",
     "items": ["OOP", "REST APIs", "IoT Systems"]},
    {"category": "ML & Data Tools", "icon": "brain-circuit",
     "items": ["TensorFlow", "OpenCV", "Scikit-learn"]},
    {"category": "Data Analysis", "icon": "bar-chart-3",
     "items": ["Pandas", "NumPy", "Matplotlib"]},
    {"category": "Embedded Systems", "icon": "cpu",
     "items": ["ESP32", "Arduino", "Real-time Sensor Processing"]},
]

# --- Experience ---
EXPERIENCE = [
    {
        "role": "Internship — Software Development",
        "company": "Croma Campus",
        "period": "Jun 2025 – Aug 2025",
        "points": [
            "Built an autonomous AI coding agent using Python and Gemini API.",
            "Implemented tool-calling loops for file analysis, code execution, "
            "and automated task completion.",
        ],
    },
    {
        "role": "IIoT Experience",
        "company": "Industrial IoT",
        "period": "Oct 2022 – Aug 2023",
        "points": [
            "Deployed Industrial IoT solutions using ThingWorx.",
            "Troubleshot hardware-software integration issues.",
            "Ensured reliable sensor network functionality.",
        ],
    },
]

# --- Education ---
EDUCATION = [
    {
        "institution": "IIMT College of Engineering, Greater Noida",
        "degree": "B.Tech in Information Technology",
        "period": "2022 – 2026",
    },
]

# --- Projects (with category for filtering) ---
PROJECTS = [
    {
        "title": "Medical Recommendation System",
        "category": "ai",
        "description": "Machine Learning-based medical recommendation platform "
                       "providing personalized medical treatments and recommendations.",
        "tech": ["Python", "Flask", "Scikit-learn", "Pandas", "HTML", "CSS", "JavaScript"],
        "github": "",
        "demo": "",
    },
    {
        "title": "Signature Forgery Detection",
        "category": "ai",
        "description": "Signature authentication system achieving 97% accuracy, "
                       "enhancing fraud detection and document verification.",
        "tech": ["Python", "OpenCV", "Machine Learning"],
        "github": "",
        "demo": "https://signature-verification-system-9e7u.onrender.com",
    },
    {
        "title": "Emotional-Logical Chatbot",
        "category": "ai",
        "description": "Flask + LangChain chatbot integrated with Groq LLM API, "
                       "supporting session-based memory.",
        "tech": ["Flask", "LangChain", "Groq API", "Python"],
        "github": "https://github.com/obaid-786/Emotional_Logical_Chatbot",
        "demo": "",
    },
    {
        "title": "Movie Management System",
        "category": "web",
        "description": "Full-stack CRUD web application with cloud-based movie "
                       "storage and search.",
        "tech": ["Python", "Flask", "SQL", "JavaScript"],
        "github": "",
        "demo": "https://movie-platform-14f8.onrender.com/",
    },
    {
        "title": "Water Management System (IoT)",
        "category": "iot",
        "description": "Reduced water wastage by 25% with real-time monitoring "
                       "using ESP32.",
        "tech": ["ESP32", "Arduino", "IoT", "Sensors"],
        "github": "",
        "demo": "",
    },
    {
        "title": "Smart Generator System (IoT)",
        "category": "iot",
        "description": "Reduced downtime by 30% by implementing predictive "
                       "analytics and remote monitoring.",
        "tech": ["ESP32", "IoT", "Predictive Analytics"],
        "github": "",
        "demo": "",
    },
]

# Categories used by the project filter UI.
PROJECT_CATEGORIES = [
    {"id": "all", "label": "All"},
    {"id": "ai", "label": "AI / ML"},
    {"id": "web", "label": "Web"},
    {"id": "iot", "label": "IoT"},
]

# --- Certifications ---
CERTIFICATIONS = [
    {"title": "Java Full Stack Development Workshop", "issuer": "Croma Campus",
     "date": "Apr 2025"},
    {"title": "Data Science & Machine Learning", "issuer": "UnCodemy", "date": ""},
    {"title": "IIOT Basic Introduction using ThingWorx", "issuer": "DCS", "date": ""},
    {"title": "Barrier Buster Bot (Centrado Kit)", "issuer": "Infosys Springboard",
     "date": ""},
    {"title": "Expert English Programme", "issuer": "SKAE India Ltd", "date": ""},
]

# --- Achievements ---
ACHIEVEMENTS = [
    "Delivered 2 high-profile IoT prototypes with complete functionality.",
    "Led end-to-end development for 4+ innovative software projects.",
    "Built AI and IoT systems solving real-world problems.",
]

# --- Contact ---
CONTACT = {
    "email": "obaidsid0@gmail.com",
    "phone": "80881681821",
    "linkedin": "https://www.linkedin.com/in/obaidullah-siddiqui-5b7718299",
    "github": "https://github.com/obaid-786",
}
