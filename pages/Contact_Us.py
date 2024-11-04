import streamlit as st

from send_email import send_email
import pandas as pd

st.header("Contact me")
df = pd.read_csv("004 topics.csv")
with st.form(key="email_form"):
	user_email = st.text_input("Your email address")
	drop_menu=st.selectbox(
		"What topic do you want to discuss",
		df["topic"])
	raw_message = st.text_area("Your message")
	message = f"""\
	Subject: New email from {user_email}
	
	From: {user_email}
	Topic {drop_menu}
"""
	button = st.form_submit_button("Submit")
	if button:
		send_email(message)
		st.info("Email sent successfully")
