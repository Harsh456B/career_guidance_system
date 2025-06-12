# roadmap_generator.py

def generate_roadmap(career, personality=None):
    career = career.lower()
    roadmap = {
        "data scientist": "1. Learn Python and SQL\n2. Master Pandas, NumPy, and data cleaning\n3. Learn ML with Scikit-learn\n4. Build portfolio projects\n5. Explore Deep Learning (PyTorch/TensorFlow)\n6. Get certified (Coursera, edX)\n7. Apply for internships/jobs",

        "software developer": "1. Learn C++/Java/Python\n2. Understand OOP and DSA\n3. Build full-stack projects\n4. Use Git and GitHub\n5. Learn frameworks (React, Django)\n6. Contribute to open-source\n7. Apply to developer roles",

        "ui ux designer": "1. Learn design principles\n2. Master Figma, Adobe XD\n3. Study UX research\n4. Create wireframes and prototypes\n5. Build a portfolio website\n6. Collaborate on design projects\n7. Apply to UI/UX internships",

        "machine learning engineer": "1. Learn Python, Stats & Math\n2. Study ML algorithms\n3. Work with Scikit-learn, TensorFlow\n4. Participate in Kaggle\n5. Build ML apps with Streamlit\n6. Create end-to-end ML projects\n7. Target ML Engineer roles"
    }

    personality_roadmap = {
        "INTJ": "Strategic learner – Prioritize structured learning paths and competitive challenges.",
        "ESTJ": "Practical learner – Use organized tools like Trello and follow timelines.",
        "ENTJ": "Leadership-focused – Take initiative in team projects and learn management tools.",
        "INFP": "Creative learner – Explore meaningful, open-ended projects and portfolios.",
        "INTP": "Analytical thinker – Dive into theory, research papers, and logic-heavy content.",
        "INFJ": "Purpose-driven – Align learning with values and social impact.",
        "ISTJ": "Detail-oriented – Focus on clear goals, checklists, and tracking progress.",
        "ENFP": "Enthusiastic learner – Blend learning with storytelling, networking, and group work.",
        "ISFP": "Hands-on explorer – Learn by building, designing, and working independently."
    }

    for key in roadmap:
        if key in career:
            base_roadmap = roadmap[key]
            personality_tip = personality_roadmap.get(personality, "")
            return base_roadmap + (f"\n\n📘 Tip for {personality}: {personality_tip}" if personality_tip else "")

    return "🚧 General roadmap coming soon... Stay tuned!"


def get_personality_description():
    return {
        "INTJ": "Introverted Intuitive Thinking Judging – Strategic, independent, logical.",
        "ESTJ": "Extraverted Sensing Thinking Judging – Practical, organized, leader.",
        "ENTJ": "Extraverted Intuitive Thinking Judging – Visionary, assertive, efficient.",
        "INFP": "Introverted Intuitive Feeling Perceiving – Creative, empathetic, idealistic.",
        "INTP": "Introverted Intuitive Thinking Perceiving – Curious, analytical, idea-driven.",
        "INFJ": "Introverted Intuitive Feeling Judging – Insightful, deep thinker, purpose-led.",
        "ISTJ": "Introverted Sensing Thinking Judging – Responsible, traditional, thorough.",
        "ENFP": "Extraverted Intuitive Feeling Perceiving – Imaginative, social, enthusiastic.",
        "ISFP": "Introverted Sensing Feeling Perceiving – Creative, gentle, spontaneous."
    }
