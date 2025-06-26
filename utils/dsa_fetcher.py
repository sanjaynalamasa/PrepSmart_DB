from utils.groq_helper import ask_groq

def get_random_dsa_question():
    prompt = "Give me a random DSA coding problem for interviews from LeetCode, GFG, or HackerRank. Include platform, title, and URL."
    return {"text": ask_groq(prompt)}
