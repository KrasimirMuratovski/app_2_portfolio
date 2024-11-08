import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
col3 = st.columns(1)

with col1:
	st.image("images/KM_photo.jpg", width=300)
with col2:
	st.title("Krasimir")
	content = '''Hi'''
	st.info(content)

content2 = 'New row'
st.write(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep = ";")
with col3:
	for index, row in df[:10].iterrows():
		st.header(row["title"])
		st.write(row["description"])
		st.image("images/"+row["image"])
		st.write(f"[Source Code]({row['url']})")
df = pd.read_csv("data.csv", sep = ";")
with col4:
	for index, row in df[10:].iterrows():
		st.header(row["title"])
		st.write(row["description"])
		st.image("images/"+row["image"])