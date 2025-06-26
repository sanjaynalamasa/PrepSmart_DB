import streamlit as st
from utils.save_user_history import login_user, signup_user

st.set_page_config(page_title="Login | PrepSmart", layout="centered")

st.title("🔐 Login or Sign Up")

form = st.form("auth_form")
email = form.text_input("Email")
password = form.text_input("Password", type="password")
action = form.radio("Action", ["Login", "Sign Up"])
submit = form.form_submit_button("Submit")

if submit:
    if action == "Login":
        user = login_user(email, password)
    else:
        user = signup_user(email, password)

    if isinstance(user, dict):
        st.session_state.user = user
        st.success("Success! Go to any section from sidebar.")
    else:
        st.error("Error: " + user)
