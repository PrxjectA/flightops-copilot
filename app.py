import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Load API key securely from .env
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say hello"}]
)

print(response.choices[0].message.content)

