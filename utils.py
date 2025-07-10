import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Suppress matplotlib deprecation warnings
import warnings
warnings.filterwarnings("ignore")


# 📊 1. Auto EDA
def auto_eda(df):
    st.subheader("📌 Dataset Summary")

    st.write("**Shape:**", df.shape)
    st.write("**Missing Values:**")
    st.write(df.isnull().sum())

    st.write("**Data Types:**")
    st.write(df.dtypes)

    st.write("**Summary Statistics:**")
    st.write(df.describe())

    st.subheader("📊 Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)


# 🤖 2. Basic ML Model Trainer (Classification)
def train_model(df):
    st.subheader("🎯 Model Training Setup")
    
    target = st.selectbox("Select the target column", df.columns)
    
    if target:
        try:
            X = pd.get_dummies(df.drop(columns=[target]))
            y = df[target]
            
            if y.dtype == "object":
                y = pd.factorize(y)[0]

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )

            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            st.success("✅ Model Trained (Random Forest Classifier)")
            st.text("📋 Classification Report:")
            st.code(classification_report(y_test, y_pred))

        except Exception as e:
            st.error(f"❌ Training Failed: {e}")
