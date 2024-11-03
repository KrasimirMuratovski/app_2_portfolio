import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
content = '''
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula 
eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient 
montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, 
pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, 
aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis 
vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. '''

st.title("The best company")
st.info(content)
st.header("Our team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("004 data.csv", sep=",")

with col1:
	for index, row in df[:4].iterrows():
		st.header(row["first name"].title() + " " + row["last name"].title())
		st.write(row["role"])
		st.image("004 images/"+row["image"])
with col2:
	for index, row in df[4:8].iterrows():
		st.header(row["first name"].title() + " " + row["last name"].title())
		st.write(row["role"])
		st.image("004 images/"+row["image"])
with col3:
	for index, row in df[8:12].iterrows():
		st.header(row["first name"].title() + " " + row["last name"].title())
		st.write(row["role"])
		st.image("004 images/"+row["image"])