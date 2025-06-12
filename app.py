# app.py
import streamlit as st
import pandas as pd
import pickle
from roadmap_generator import generate_roadmap

# Set page config
st.set_page_config(page_title="SkillPath AI - Career Guidance System", layout="wide")

# Custom CSS for light purple + white theme
st.markdown("""
    <style>
        body {
            background-color: #f8f4fc;
        }
        .main {
            background-color: #ffffff;
            color: #222222;
        }
        .stButton>button {
            background-color: #6c4fbb;
            color: white;
            border-radius: 8px;
        }
        .stTextInput>div>input {
            background-color: #f0ebf8;
        }
        .stSelectbox>div>div>div {
            background-color: #f0ebf8;
        }
    </style>
""", unsafe_allow_html=True)

# Load model
model_path = "model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

st.title("🚀 SkillPath AI – Intelligent Career Guidance System")
st.markdown("**Please enter your information below to get personalized career guidance.**")

# Load sample dataset to extract feature inputs
data_path = "data/career_dataset_7000.csv"
df = pd.read_csv(data_path)

# Detect target and drop it from features
target_col = [col for col in df.columns if "career" in col.lower()][0]
if "Name" in df.columns:
    feature_df = df.drop(columns=[target_col, "Name"])
else:
    feature_df = df.drop(columns=[target_col])

# Add Personality Type Descriptions
def get_personality_description(ptype):
    descriptions = {
        "INTJ": "Introverted, Intuitive, Thinking, Judging – Strategic and logical planners.",
        "ESTJ": "Extroverted, Sensing, Thinking, Judging – Organized and take-charge leaders.",
        "ENTJ": "Extroverted, Intuitive, Thinking, Judging – Confident and charismatic leaders.",
        "INFP": "Introverted, Intuitive, Feeling, Perceiving – Idealistic and empathetic creatives.",
        "INTP": "Introverted, Intuitive, Thinking, Perceiving – Analytical and curious thinkers.",
        "INFJ": "Introverted, Intuitive, Feeling, Judging – Visionary and insightful advocates.",
        "ISTJ": "Introverted, Sensing, Thinking, Judging – Responsible and detail-oriented.",
        "ENFP": "Extroverted, Intuitive, Feeling, Perceiving – Energetic and imaginative explorers.",
        "ISFP": "Introverted, Sensing, Feeling, Perceiving – Gentle, artistic, and quiet nurturers."
    }
    return descriptions.get(ptype, "")

# Collect input features
def user_inputs():
    input_data = {}
    for col in feature_df.columns:
        if df[col].dtype == 'object':
            val = st.selectbox(f"Select your {col}", options=df[col].unique())
            input_data[col] = val
            if col.lower() == "personality type":
                desc = get_personality_description(val)
                if desc:
                    st.markdown(f"🧠 **{val}**: {desc}")
        else:
            input_data[col] = st.number_input(f"Enter your {col}", min_value=0, max_value=100, step=1)
    return pd.DataFrame([input_data])

input_df = user_inputs()

# Predict button
if st.button("🎯 Get Career Recommendation"):
    try:
        input_encoded = pd.get_dummies(input_df)
        model_features = model.feature_names_in_

        for feature in model_features:
            if feature not in input_encoded.columns:
                input_encoded[feature] = 0

        input_encoded = input_encoded[model_features]
        prediction = model.predict(input_encoded)[0]

        st.success(f"🧠 Recommended Career Path: **{prediction}**")

        st.markdown("---")
        st.subheader("📘 Personalized Learning Roadmap")
        roadmap_text = generate_roadmap(prediction)
        st.markdown(roadmap_text)

        if "general" in roadmap_text.lower():
            st.warning("📌 We’re constantly improving our guidance. Your career roadmap will be personalized soon!")

    except Exception as e:
        st.error(f"❌ Error: {e}")