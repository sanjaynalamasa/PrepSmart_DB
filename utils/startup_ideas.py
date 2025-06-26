from utils.groq_helper import ask_groq

def get_startup_idea():
    prompt = "Generate a random startup product or service idea and explain it in 2-3 sentences."
    return {"text": ask_groq(prompt)}
