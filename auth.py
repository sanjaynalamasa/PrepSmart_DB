import streamlit as st
import pyrebase

# Firebase Config (replace with your own values from Firebase console)
firebase_config = {
    "apiKey": st.secrets["firebase_api_key"],
    "authDomain": st.secrets["firebase_auth_domain"],
    "projectId": st.secrets["firebase_project_id"],
    "storageBucket": st.secrets["firebase_storage_bucket"],
    "messagingSenderId": st.secrets["firebase_messaging_sender_id"],
    "appId": st.secrets["firebase_app_id"],
    "measurementId": st.secrets["firebase_measurement_id"],
    "databaseURL": ""  # Leave empty if using only auth and Firestore
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def login_signup_page():
    st.title("🔐 Login or Signup to Continue")
    choice = st.radio("Select Option", ["Login", "Signup"], horizontal=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if choice == "Signup":
        if st.button("Create Account"):
            try:
                auth.create_user_with_email_and_password(email, password)
                st.success("Account created successfully. Please login.")
            except Exception as e:
                st.error(f"Signup failed: {e}")

    elif choice == "Login":
        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state.logged_in = True
                st.session_state.email = email
                st.session_state.user = user
                st.rerun()
            except Exception as e:
                st.error(f"Login failed: {e}")

def is_logged_in():
    return st.session_state.get("logged_in", False)

def logout():
    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.rerun()
