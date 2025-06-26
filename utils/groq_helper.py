import openai
import streamlit as st

# Fetch API Key securely from Streamlit Secrets
API_KEY = st.secrets["groq_api_key"]

client = openai.OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def ask_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="mistral-saba-24b",  # or use any supported Groq model
            messages=[
                {"role": "system", "content": "You are an AI assistant helping with interview preparation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"
