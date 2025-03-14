import streamlit as st

st.set_page_config(page_title="test", page_icon=":shark:", layout="wide")

st.markdown("# Hello World!")
st.sidebar.markdown("Home")

from PIL import Image
im = Image.open('Dell_logo.png')
st.sidebar.image(im, width=100)
