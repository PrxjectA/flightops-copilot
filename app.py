import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Classic style — best for Streamlit Cloud
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say hello"}]
)

print(response.choices[0].message["content"])

