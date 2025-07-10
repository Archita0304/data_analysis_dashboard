import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import random

st.set_page_config(layout="wide")
st.title("📈 Smart Visual Dashboard (Grid View)")

# Check for dataset
if "df" not in st.session_state:
    st.warning("Please upload or select a dataset from the main page.")
    st.stop()

df = st.session_state.df

# Identify columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

# Default selections
default_num = random.choice(numeric_cols) if numeric_cols else None
default_cat = random.choice(cat_cols) if cat_cols else None
second_num = random.choice([col for col in numeric_cols if col != default_num]) if len(numeric_cols) > 1 else default_num

# Dropdowns for user to change features
st.markdown("### 🔧 Customize Features (or leave default)")

col1, col2, col3 = st.columns(3)
with col1:
    selected_num = st.selectbox("📊 Select numeric feature", numeric_cols, index=numeric_cols.index(default_num) if default_num in numeric_cols else 0)
with col2:
    selected_cat = st.selectbox("🔤 Select categorical feature", cat_cols, index=cat_cols.index(default_cat) if default_cat in cat_cols else 0)
with col3:
    num2 = st.selectbox("📊 Select second numeric feature", numeric_cols, index=numeric_cols.index(second_num) if second_num in numeric_cols else 0)

# Validate selections
if selected_cat not in df.columns or selected_num not in df.columns or num2 not in df.columns:
    st.error("One or more selected columns are missing in the dataset.")
    st.stop()

# ---------------------- Grid Layout ------------------------

# Top Grid: Heatmap & Pie Chart
grid1, grid2 = st.columns(2)

with grid1:
    st.subheader("🔗 Correlation Heatmap")
    if selected_num != num2:
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.heatmap(df[[selected_num, num2]].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.info("Choose two different numeric columns for a correlation heatmap.")

with grid2:
    st.subheader(f"🥧 Pie Chart: {selected_cat}")
    pie_df = df[selected_cat].value_counts().head(5).reset_index()
    pie_df.columns = [selected_cat, "count"]
    fig = px.pie(pie_df, names=selected_cat, values="count", title=f"{selected_cat} distribution")
    st.plotly_chart(fig, use_container_width=True)

# Bottom Grid: Bar & Histogram
grid3, grid4 = st.columns(2)

with grid3:
    st.subheader(f"📶 Bar Chart: {selected_cat}")
    bar_data = df[selected_cat].value_counts().head(10)
    st.bar_chart(bar_data)

with grid4:
    st.subheader(f"📊 Histogram: {selected_num}")
    fig, ax = plt.subplots(figsize=(6, 3))
    sns.histplot(df[selected_num], kde=True, ax=ax)
    st.pyplot(fig)

# Extra Grid: Box & Line Chart
grid5, grid6 = st.columns(2)

with grid5:
    st.subheader(f"📦 Box Plot: {selected_num}")
    fig, ax = plt.subplots(figsize=(6, 3))
    sns.boxplot(y=df[selected_num], ax=ax)
    st.pyplot(fig)

with grid6:
    st.subheader(f"📈 Line Chart: {selected_num}")
    st.line_chart(df[selected_num])
