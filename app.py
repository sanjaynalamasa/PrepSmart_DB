import streamlit as st
from utils.groq_helper import ask_groq
from auth import login_signup_page, is_logged_in, logout
from utils.save_user_history import save_user_history

st.set_page_config(page_title="PrepSmart - AI Interview Coach", layout="wide")

if not is_logged_in():
    login_signup_page()
    st.stop()

logout()
st.title("🎓 PrepSmart: Your AI Interview Preparation Assistant")

# Load styles
st.markdown("<style>" + open("assets/styles.css").read() + "</style>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
section = st.sidebar.radio("Go to", [
    "Random DSA Question",
    "Computer Fundamentals",
    "Aptitude & Reasoning",
    "Startup Product/Service Prep",
    "🎯 I'm Feeling Lucky!"
])

def show_code_ide_links():
    st.markdown("""
        **Try this on:**
        - [💻 Replit](https://replit.com/)
        - [👨‍💻 CodeChef IDE](https://www.codechef.com/ide)
        - [⚡ LeetCode Playground](https://leetcode.com/playground)
    """)

# --- DSA ---
if section == "Random DSA Question":
    st.header("🔢 Random DSA Problem")
    if st.button("🎲 Next DSA Question") or "dsa_q" not in st.session_state:
        st.session_state.dsa_q = ask_groq(
            "Give me a random DSA coding problem from LeetCode, GFG, or HackerRank with title, platform, description, and URL."
        )
        save_user_history(st.session_state.email, {"type": "DSA", "content": st.session_state.dsa_q})
    st.markdown(st.session_state.dsa_q)
    show_code_ide_links()
    with st.expander("💬 Ask something about this DSA problem"):
        user_query = st.text_input("Your question:", key="dsa_chat")
        if user_query:
            response = ask_groq(user_query)
            st.success(response)

# --- CS Fundamentals ---
elif section == "Computer Fundamentals":
    st.header("💻 CS Fundamental Question")
    topic = st.selectbox("Choose Topic", ["OS", "DBMS", "CN", "OOPs"])
    key = f"cs_{topic.lower()}"
    if st.button("🔄 Next Question") or key not in st.session_state:
        st.session_state[key] = ask_groq(f"Give me a technical interview question with answer from {topic}.")
        save_user_history(st.session_state.email, {"type": f"CS - {topic}", "content": st.session_state[key]})
    st.markdown(st.session_state[key])
    with st.expander("💬 Ask something about this CS topic"):
        user_query = st.text_input("Your question:", key="cs_chat")
        if user_query:
            response = ask_groq(user_query)
            st.success(response)

# --- Aptitude ---
elif section == "Aptitude & Reasoning":
    st.header("🧠 Aptitude & Reasoning")
    company = st.selectbox("Select Company", ["TCS", "Infosys", "Wipro", "Cognizant"])
    key = f"apt_{company.lower()}"
    if st.button("🔄 Next Aptitude Question") or key not in st.session_state:
        st.session_state[key] = ask_groq(f"Give me one aptitude or reasoning question with solution asked in {company} interviews.")
        save_user_history(st.session_state.email, {"type": f"Aptitude - {company}", "content": st.session_state[key]})
    st.markdown(st.session_state[key])
    with st.expander("💬 Ask something about this aptitude question"):
        user_query = st.text_input("Your question:", key="apt_chat")
        if user_query:
            response = ask_groq(user_query)
            st.success(response)

# --- Startup Ideas ---
elif section == "Startup Product/Service Prep":
    st.header("🚀 Startup Product or Service Idea")
    if st.button("💡 Next Startup Idea") or "startup_idea" not in st.session_state:
        st.session_state.startup_idea = ask_groq("Generate a unique startup product or service idea and explain it in 2-3 sentences for an interview pitch.")
        save_user_history(st.session_state.email, {"type": "Startup", "content": st.session_state.startup_idea})
    st.markdown(st.session_state.startup_idea)
    with st.expander("💬 Ask something about this startup idea"):
        user_query = st.text_input("Your question:", key="startup_chat")
        if user_query:
            response = ask_groq(user_query)
            st.success(response)

# --- I'm Feeling Lucky ---
elif section == "🎯 I'm Feeling Lucky!":
    st.header("🎯 Surprise Combo Round")
    if st.button("🎰 Shuffle All"):
        st.session_state.combo_dsa = ask_groq("Give me a random DSA coding problem from LeetCode, GFG, or HackerRank with title, platform, and URL.")
        st.session_state.combo_cs = ask_groq("Give me a CS fundamentals interview question and answer. Randomly pick from OS, DBMS, CN, or OOPs.")
        st.session_state.combo_apt = ask_groq("Give me a company-specific aptitude or reasoning interview question with solution.")
        st.session_state.combo_startup = ask_groq("Generate a random startup product or service idea and explain it briefly.")

        save_user_history(st.session_state.email, {
            "type": "Lucky Combo",
            "content": {
                "DSA": st.session_state.combo_dsa,
                "CS": st.session_state.combo_cs,
                "Aptitude": st.session_state.combo_apt,
                "Startup": st.session_state.combo_startup
            }
        })

    st.subheader("🔢 DSA:")
    st.markdown(st.session_state.get("combo_dsa", "Click 'Shuffle All' to begin"))

    st.subheader("💻 CS Fundamentals:")
    st.markdown(st.session_state.get("combo_cs", ""))

    st.subheader("🧠 Aptitude:")
    st.markdown(st.session_state.get("combo_apt", ""))

    st.subheader("🚀 Startup Idea:")
    st.markdown(st.session_state.get("combo_startup", ""))

    with st.expander("💬 Ask anything about this combo"):
        user_query = st.text_input("Your question:", key="combo_chat")
        if user_query:
            response = ask_groq(user_query)
            st.success(response)
