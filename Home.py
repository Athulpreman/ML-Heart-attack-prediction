import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import streamlit.components.v1 as components




st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)
st.sidebar.write("")


st.markdown("# Welcome to Heart Attack prediction")
image = Image.open('hrt.webp')
st.image(image)
st.sidebar.title("Introduction")
st.sidebar.write("Here main aim of heart attack prediction project is to eliminate the need of consulting a doctor before the confirmation of the data.")
st.sidebar.write("We can use this simple page for predicting the possibility of heart attack directly.")
st.sidebar.write("We can consult the doctor directly with the results.")