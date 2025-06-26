from utils.groq_helper import ask_groq

def get_cs_question(topic):
    prompt = f"Give me a technical interview question with answer from {topic} (like OS, DBMS, CN, or OOPs)."
    return {"text": ask_groq(prompt)}
