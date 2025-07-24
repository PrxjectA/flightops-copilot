import openai
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Page config
st.set_page_config(page_title="✈️ FlightOps Copilot", page_icon="🛩", layout="centered")

# Header
st.markdown("""
    <div style="text-align: center;">
        <h1 style="font-size: 3em;">🧑‍✈️ FlightOps Copilot</h1>
        <p style="font-size: 1.2em; color: gray;">Your AI assistant for fast, professional trip briefings in private aviation.</p>
        <hr style="border-top: 1px solid #ccc;">
    </div>
""", unsafe_allow_html=True)

# Input
with st.form(key="brief_form"):
    user_input = st.text_area("📝 Enter a trip scenario (e.g., 'Flight from Houston to Geneva with 6 passengers')", height=150)
    submit = st.form_submit_button("🚀 Generate Trip Brief")

# AI response
if submit and user_input:
    try:
        with st.spinner("Generating your trip brief..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert private aviation operations planner. Generate clear, concise trip briefs using professional aviation language."},
                    {"role": "user", "content": user_input}
                ]
            )
            brief = response.choices[0].message.content

        st.markdown("## ✈️ Trip Brief Generated")
        st.markdown("## 📝 Trip Brief Generated")
st.markdown(f"""
    <div style='
        background-color: #111111;
        color: #f0f0f0;
        padding: 30px;
        border-radius: 14px;
        font-size: 1.15em;
        line-height: 1.8;
        font-family: "Segoe UI", "Helvetica Neue", sans-serif;
        white-space: pre-wrap;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    '>
        {brief}
    </div>
""", unsafe_allow_html=True)


    except Exception as e:
        st.error(f"❌ Error generating brief: {e}")
