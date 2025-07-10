import streamlit as st
from utils import train_model

st.title("🧠 Train a Machine Learning Model")

if "df" in st.session_state:
    df = st.session_state.df
    train_model(df)
else:
    st.warning("Please upload a dataset from the main page.")
