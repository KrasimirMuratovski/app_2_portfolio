import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
	st.image("images/KM_photo.jpg", width=300)
with col2:
	st.title("Krasimir")
	content = '''Hi'''
	st.info(content)