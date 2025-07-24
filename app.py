import openai
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit page config
st.set_page_config(page_title="FlightOps Copilot ✈️", layout="centered")

st.title("🧑‍✈️ FlightOps Copilot")
st.write("Generate an AI-powered trip brief below:")

# User input
user_input = st.text_input("Enter a trip prompt (e.g. 'Flight from Houston to Geneva with 6 passengers')")

if user_input:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert flight planner generating trip briefs."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message["content"]
        st.subheader("📝 Trip Brief")
        st.write(reply)
    except Exception as e:
        st.error(f"Error generating brief: {e}")
