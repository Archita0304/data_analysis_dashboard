import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Data Assistant", layout="wide")
st.title("📊 Data Analysis Assistant Dashboard")

# Ensure datasets folder exists
os.makedirs("dataset", exist_ok=True)

# List available datasets
dataset_files = [f for f in os.listdir("dataset") if f.endswith((".csv", ".xlsx"))]

# Dataset selector from local folder
st.subheader("📁 Select a dataset from local 'dataset/' folder")
selected_file = st.selectbox("Choose a dataset", options=["--Select--"] + dataset_files)

if selected_file != "--Select--":
    file_path = os.path.join("dataset", selected_file)
    try:
        if selected_file.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif selected_file.endswith(".xlsx"):
            df = pd.read_excel(file_path)

        st.session_state.df = df
        st.success(f"✅ Loaded: {selected_file}")
        st.dataframe(df.head())

    except Exception as e:
        st.error(f"❌ Failed to load: {e}")
else:
    st.info("Please select a dataset from the list above.")

st.markdown("---")
st.markdown("Navigate using the sidebar to explore Visuals and Train ML models.")
