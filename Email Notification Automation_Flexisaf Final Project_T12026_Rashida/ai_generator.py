# ai_generator.py
# Generates personalized message using AI

from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_message(name, announcement):
    prompt = f"Write a friendly school notification email to {name} about: {announcement}"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content