import streamlit as st

st.title("📊 Dataset Overview")

if "df" in st.session_state:
    df = st.session_state.df
    st.write("### Preview")
    st.dataframe(df.head())

    st.write("### Basic Info")
    st.write(f"Shape: {df.shape}")
    st.write("Missing Values:")
    st.write(df.isnull().sum())
    st.write("### Summary Statistics")
    st.write(df.describe())
else:
    st.warning("Please upload a dataset from the main page.")
