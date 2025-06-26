import streamlit as st
import pyrebase
from utils.save_user_history import get_user_data

# Firebase Config from secrets.toml
firebase_config = st.secrets["firebase"]
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Initialize session state
if "user" not in st.session_state:
    st.session_state.user = None

def login_signup_page():
    st.set_page_config(page_title="Login | PrepSmart", layout="centered")
    st.title("🔐 Login or Signup to Continue")

    choice = st.radio("Select Option", ["Login", "Signup"], horizontal=True)
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if choice == "Signup":
        if st.button("Create Account"):
            try:
                auth.create_user_with_email_and_password(email, password)
                st.success("Account created successfully! Please login.")
            except Exception as e:
                st.error("Signup Failed: " + str(e))
    else:
        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state.user = user
                st.success("Login successful! Redirecting...")
                st.rerun()
            except Exception as e:
                st.error("Login Failed: " + str(e))

# Show login/signup if user not logged in
if not st.session_state.user:
    login_signup_page()
else:
    st.switch_page("app.py")
