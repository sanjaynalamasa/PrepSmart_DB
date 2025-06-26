# import pyrebase
# import streamlit as st
# from datetime import datetime
# import firebase_admin
# from firebase_admin import credentials, firestore

# # Firebase configuration
# firebase_config = {
#     "apiKey": st.secrets["firebase_api_key"],
#     "authDomain": st.secrets["firebase_auth_domain"],
#     "projectId": st.secrets["firebase_project_id"],
#     "storageBucket": st.secrets["firebase_storage_bucket"],
#     "messagingSenderId": st.secrets["firebase_messaging_sender_id"],
#     "appId": st.secrets["firebase_app_id"],
#     "databaseURL": ""  # Optional
# }

# # Initialize Pyrebase
# firebase = pyrebase.initialize_app(firebase_config)
# auth = firebase.auth()

# # Initialize Firebase Admin SDK
# if not firebase_admin._apps:
#     cred = credentials.Certificate("serviceAccountKey.json")
#     firebase_admin.initialize_app(cred)

# db = firestore.client()

# def signup_user(email, password):
#     try:
#         user = auth.create_user_with_email_and_password(email, password)
#         return user
#     except Exception as e:
#         st.error(f"Signup failed: {e}")
#         return None

# def login_user(email, password):
#     try:
#         user = auth.sign_in_with_email_and_password(email, password)
#         return user
#     except Exception as e:
#         st.error(f"Login failed: {e}")
#         return None

# def save_user_history(email, data):
#     try:
#         doc_ref = db.collection("user_history").document(email)
#         doc = doc_ref.get()
#         if doc.exists:
#             doc_ref.update({
#                 "history": firestore.ArrayUnion([{
#                     "timestamp": datetime.now().isoformat(),
#                     **data
#                 }])
#             })
#         else:
#             doc_ref.set({
#                 "history": [{
#                     "timestamp": datetime.now().isoformat(),
#                     **data
#                 }]
#             })
#     except Exception as e:
#         print(f"Failed to store history: {e}")



































# import pyrebase
# import streamlit as st
# from datetime import datetime
# import firebase_admin
# from firebase_admin import credentials, firestore

# # Firebase configuration
# firebase_config = {
#     "apiKey": st.secrets["firebase_api_key"],
#     "authDomain": st.secrets["firebase_auth_domain"],
#     "projectId": st.secrets["firebase_project_id"],
#     "storageBucket": st.secrets["firebase_storage_bucket"],
#     "messagingSenderId": st.secrets["firebase_messaging_sender_id"],
#     "appId": st.secrets["firebase_app_id"],
#     "databaseURL": ""  # Optional
# }

# # Initialize Pyrebase
# firebase = pyrebase.initialize_app(firebase_config)
# auth = firebase.auth()

# # Initialize Firebase Admin SDK
# if not firebase_admin._apps:
#     cred = credentials.Certificate("serviceAccountKey.json")
#     firebase_admin.initialize_app(cred)

# db = firestore.client()

# def signup_user(email, password):
#     try:
#         user = auth.create_user_with_email_and_password(email, password)
#         return user
#     except Exception as e:
#         st.error(f"Signup failed: {e}")
#         return None

# def login_user(email, password):
#     try:
#         user = auth.sign_in_with_email_and_password(email, password)
#         return user
#     except Exception as e:
#         st.error(f"Login failed: {e}")
#         return None

# def store_user_history(email, data):
#     try:
#         doc_ref = db.collection("user_history").document(email)
#         doc = doc_ref.get()
#         if doc.exists:
#             doc_ref.update({
#                 "history": firestore.ArrayUnion([{
#                     "timestamp": datetime.now().isoformat(),
#                     **data
#                 }])
#             })
#         else:
#             doc_ref.set({
#                 "history": [{

#                     "timestamp": datetime.now().isoformat(),
#                     **data
#                 }]
#             })
#     except Exception as e:
#         print(f"Failed to store history: {e}")

# # ✅ FIXED: This function supports 3 arguments from app.py
# def save_user_history(email, content_type, content):
#     data = {
#         "type": content_type,
#         "content": content
#     }
#     store_user_history(email, data)



























# # utils/firebase_helper.py
# import pyrebase
# import streamlit as st
# from datetime import datetime
# import firebase_admin
# from firebase_admin import credentials, firestore

# # Firebase configuration
# firebase_config = {
#     "apiKey": st.secrets["firebase_api_key"],
#     "authDomain": st.secrets["firebase_auth_domain"],
#     "projectId": st.secrets["firebase_project_id"],
#     "storageBucket": st.secrets["firebase_storage_bucket"],
#     "messagingSenderId": st.secrets["firebase_messaging_sender_id"],
#     "appId": st.secrets["firebase_app_id"],
#     "databaseURL": ""
# }

# firebase = pyrebase.initialize_app(firebase_config)
# auth = firebase.auth()

# # Admin SDK
# if not firebase_admin._apps:
#     cred = credentials.Certificate("serviceAccountKey.json")
#     firebase_admin.initialize_app(cred)

# db = firestore.client()

# def signup_user(email, password):
#     try:
#         user = auth.create_user_with_email_and_password(email, password)
#         return user
#     except Exception as e:
#         st.error(f"Signup failed: {e}")
#         return None

# def login_user(email, password):
#     try:
#         user = auth.sign_in_with_email_and_password(email, password)
#         return user
#     except Exception as e:
#         st.error(f"Login failed: {e}")
#         return None

# def save_user_history(email, data):
#     try:
#         doc_ref = db.collection("user_history").document(email)
#         doc = doc_ref.get()
#         history_entry = {
#             "timestamp": datetime.now().isoformat(),
#             **data
#         }
#         if doc.exists:
#             doc_ref.update({"history": firestore.ArrayUnion([history_entry])})
#         else:
#             doc_ref.set({"history": [history_entry]})
#     except Exception as e:
#         print(f"Failed to store history: {e}")










































# # utils/firebase_helper.py
# import pyrebase
# import streamlit as st
# from datetime import datetime
# import firebase_admin
# from firebase_admin import credentials, firestore

# # Firebase client config for auth via pyrebase
# firebase_config = {
#     "apiKey": st.secrets["firebase_api_key"],
#     "authDomain": st.secrets["firebase_auth_domain"],
#     "projectId": st.secrets["firebase_project_id"],
#     "storageBucket": st.secrets["firebase_storage_bucket"],
#     "messagingSenderId": st.secrets["firebase_messaging_sender_id"],
#     "appId": st.secrets["firebase_app_id"],
#     "databaseURL": ""  # Optional if you're not using RTDB
# }

# firebase = pyrebase.initialize_app(firebase_config)
# auth = firebase.auth()

# # Firebase Admin SDK initialization from secrets
# if not firebase_admin._apps:
#     cred = credentials.Certificate(st.secrets["firebase_service_account"])
#     firebase_admin.initialize_app(cred)

# db = firestore.client()

# # Signup function
# def signup_user(email, password):
#     try:
#         user = auth.create_user_with_email_and_password(email, password)
#         return user
#     except Exception as e:
#         st.error(f"Signup failed: {e}")
#         return None

# # Login function
# def login_user(email, password):
#     try:
#         user = auth.sign_in_with_email_and_password(email, password)
#         return user
#     except Exception as e:
#         st.error(f"Login failed: {e}")
#         return None

# # Save user history to Firestore
# def save_user_history(email, data):
#     try:
#         doc_ref = db.collection("user_history").document(email)
#         doc = doc_ref.get()
#         history_entry = {
#             "timestamp": datetime.now().isoformat(),
#             **data
#         }
#         if doc.exists:
#             doc_ref.update({"history": firestore.ArrayUnion([history_entry])})
#         else:
#             doc_ref.set({"history": [history_entry]})
#     except Exception as e:
#         print(f"Failed to store history: {e}")
















































# utils/save_user_history.py

import pyrebase
import streamlit as st
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase config for Pyrebase
firebase_config = {
    "apiKey": st.secrets["firebase_api_key"],
    "authDomain": st.secrets["firebase_auth_domain"],
    "projectId": st.secrets["firebase_project_id"],
    "storageBucket": st.secrets["firebase_storage_bucket"],
    "messagingSenderId": st.secrets["firebase_messaging_sender_id"],
    "appId": st.secrets["firebase_app_id"],
    "databaseURL": ""
}

# Initialize Pyrebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Initialize Firebase Admin with credentials from secrets
if not firebase_admin._apps:
    cred = credentials.Certificate(dict(st.secrets["firebase_service_account"]))
    firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

def signup_user(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return user
    except Exception as e:
        st.error(f"Signup failed: {e}")
        return None

def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except Exception as e:
        st.error(f"Login failed: {e}")
        return None

def save_user_history(email, data):
    try:
        doc_ref = db.collection("user_history").document(email)
        doc = doc_ref.get()
        history_entry = {
            "timestamp": datetime.now().isoformat(),
            **data
        }
        if doc.exists:
            doc_ref.update({"history": firestore.ArrayUnion([history_entry])})
        else:
            doc_ref.set({"history": [history_entry]})
    except Exception as e:
        print(f"Failed to store history: {e}")
