import streamlit as st
from send_email import send_email

st.title("Contact Us")
st.write("Send us a message or reach out via email.")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email goes here")

    topic = st.selectbox(
        "What topic do you want to discuss?",
        ("Job Inquiry", "Project Collaboration", "Bug Report", "Other"))

    raw_message = st.text_area("Text")
    message = f"""\
Subject: new email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("submit")
    print(button)
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
