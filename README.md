# 📊 Data Analysis Dashboard

A powerful and user-friendly web-based **data analysis assistant** built using **Streamlit**, allowing users to upload datasets, explore data through visualizations, and even train machine learning models using Kaggle datasets — all from a single dashboard.

---

## 🚀 Features

- ✅ Upload datasets in `.csv` or `.xlsx` format
- ✅ Automatically load datasets from the `dataset/` folder
- ✅ Dynamic, grid-style dashboard
- ✅ Feature selection for focused analysis
- ✅ Visualizations include:
  - 📌 Heatmap
  - 📊 Pie Chart
  - 📈 Line Chart
  - 📉 Bar Chart
  - 🔗 Correlation Matrix
- ✅ Model training using uploaded datasets
- ✅ Direct links to Kaggle for dataset access

---

## 🗂️ Folder Structure
```
data_analysis_dashboard/
├── app.py # Main Streamlit app interface
├── pages/ # Streamlit multi-page setup
│ ├── visual.py # Visualizations (heatmap, charts)
│ ├── overview.py # Dataset overview and summary
│ └── train.py # Model training page
├── utils.py # Utility functions for plotting, processing
├── dataset/ # Folder for uploaded datasets
│ ├── salaries.csv
│ ├── sales_data.csv
│ └── teen_phone_addiction_dataset.csv
└── README.md # Project documentation
```
---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Archita0304/data_analysis_dashboard.git
cd data_analysis_dashboard
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### Run the App
```bash
streamlit run app.py
```
Once running, the app will open in your default web browser. You can:<br>
--Upload new datasets<br>
--Select existing datasets from the dataset/ folder<br>
--Explore various types of visualizations<br>
--View all charts in a grid layout<br>
--Change features dynamically for live updates<br>

---
🧠 Notes<br>
You can place any number of .csv or .xlsx files in the dataset/ folder — they’ll automatically be detected.<br>
The dashboard displays random visualizations on load and allows users to change the feature.<br>
Kaggle datasets can be manually downloaded and placed into the dataset/ folder.<br>


