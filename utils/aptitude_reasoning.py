from utils.groq_helper import ask_groq

def get_aptitude_question(company):
    prompt = f"Give one aptitude or reasoning question with solution asked in {company} interviews."
    return {"text": ask_groq(prompt)}
