# 🌳 Urban Tree Health Monitoring & Smart Plantation Recommendation System

> An end-to-end **Machine Learning** project that predicts **Tree Health Status**, **Tree Growth Rate**, **Carbon Absorption**, and **Tree Survival Probability**, while recommending the most suitable tree species for plantation based on environmental and biological conditions.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)
![CatBoost](https://img.shields.io/badge/CatBoost-Classifier-yellow?style=for-the-badge)
![XGBoost](https://img.shields.io/badge/XGBoost-Regressor-orange?style=for-the-badge)

---

# 📖 Project Overview

Urban trees improve air quality, reduce pollution, absorb carbon dioxide, lower urban temperatures, and enhance biodiversity. However, manually monitoring tree health and selecting suitable trees for plantation is time-consuming and expensive.

This project leverages **Machine Learning** to automate urban tree monitoring and decision-making through four predictive models and one recommendation system.

The application is built using **Python**, **Streamlit**, **CatBoost**, and **XGBoost**, providing an interactive dashboard for tree analysis.

---

# 🎯 Objectives

- Predict the health status of urban trees.
- Predict tree growth rate.
- Estimate annual carbon absorption.
- Predict tree survival probability.
- Recommend suitable tree species for plantation.
- Support sustainable urban forestry and smart city planning.

---

# 🚀 Features

## 🌳 Tree Health Status Prediction

Predicts the health condition of a tree.

### Model

✅ CatBoost Classifier

### Output

- Healthy
- Moderate
- Unhealthy

---

## 📈 Tree Growth Rate Prediction

Predicts future growth of the tree.

### Model

✅ XGBoost Regressor

### Output

- Growth Rate
- Estimated Height Growth
- Development Trend

---

## 🌍 Carbon Absorption Prediction

Predicts the annual carbon dioxide absorbed by a tree.

### Model

✅ XGBoost Regressor

### Output

- Carbon Absorption (kg/year)

---

## 🌱 Tree Survival Probability Prediction

Predicts the survival probability of a tree based on environmental conditions.

### Model

✅ CatBoost Regressor

### Output

- Survival Probability (%)

---

## 🌿 Plantation Recommendation System

Recommends the most suitable tree species based on environmental conditions using a rule-based recommendation engine.

Recommendation Factors:

- Temperature
- Rainfall
- Soil Moisture
- Pollution Level
- Sunlight
- Available Space
- Root Depth
- Canopy Width

---

# 🤖 Machine Learning Models

| Module | Algorithm |
|---------|-----------|
| Tree Health Status | CatBoost Classifier |
| Tree Growth Rate | XGBoost Regressor |
| Carbon Absorption | XGBoost Regressor |
| Survival Probability | CatBoost Regressor |
| Tree Recommendation | Rule-Based System |

---

# 📊 Dataset Features

### 🌳 Tree Information

- Tree Name
- Tree Age
- Height (Meter)
- Trunk Diameter (cm)
- Canopy Width (m)
- Root Depth (m)

### 🌿 Biological Features

- Leaf Color
- Root Condition
- Disease Symptoms
- Pest Presence

### 🌍 Environmental Features

- Temperature
- Rainfall
- Soil Moisture
- Humidity
- Wind Speed
- Air Pollution
- Sunlight Exposure

---

# 📈 Machine Learning Workflow

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Label Encoding
      │
      ▼
Train/Test Split
      │
      ▼
Model Training
      │
      ├───────────────┐
      ▼               ▼
 CatBoost         XGBoost
      │               │
      ▼               ▼
Prediction Models
      │
      ▼
Streamlit Deployment
```

---

# 📊 Model Evaluation

## Classification

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

## Regression

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| Pandas | Data Analysis |
| NumPy | Numerical Computing |
| Scikit-learn | Data Preprocessing |
| CatBoost | Classification & Regression |
| XGBoost | Regression Models |
| Plotly | Interactive Dashboard |
| Matplotlib | Data Visualization |
| Joblib | Model Serialization |

---

# 📁 Project Structure

```
Urban-Tree-Health-Monitoring-System/
│
├── data/
│   ├── clean_data/
│   │   └── encode_tree_dataset_final.csv
│   │
│   └── raw_data/
│       └── trees_indian_dataset.csv
│
├── images/
│   └── logo.png
│
├── models/
│   ├── CarbonPrediction_Feature_Columns.pkl
│   ├── Carbon_Prediction_Model.pkl
│   ├── frequency_maps.pkl
│   ├── Growth_feature_columns.pkl
│   ├── Growth_Prediction_Model.pkl
│   ├── label_encoder.pkl
│   ├── ordinal_encoder.pkl
│   ├── Survival_feature_columns.pkl
│   ├── Survival_Prediction_Model.pkl
│   ├── Tree_Health_Classification_Model.pkl
│   └── Tree_Health_Prediction_Feature_Columns.pkl
│
├── notebooks/
│   ├── catboost info/
│   ├── CarbonPrediction_Model.ipynb
│   ├── encoder.ipynb
│   ├── Exploratory_Data_Analysis.ipynb
│   ├── Growth_Prediction_Model.ipynb
│   ├── Survival_Prediction_Model.ipynb
│   └── Tree_Health_Classification_Model.ipynb
│
├── pages/
│   ├── 1_Health_Prediction.py
│   ├── 2_Growth_Prediction.py
│   ├── 3_Carbon_Prediction.py
│   ├── 4_Survival_Prediction.py
│   └── 5_Tree_Recommendation.py
│
├── utility/
├── Home.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/vipul892/Urban-Tree-Health-Monitoring-System.git
```

Move to project folder

```bash
cd Urban-Tree-Health-Monitoring-System
```

Create virtual environment (Optional)

```bash
python -m venv venv
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run Home.py
```

---

# 📸 Application Modules

- 🏠 Home
- 🌳 Tree Health Prediction
- 📈 Tree Growth Prediction
- 🌍 Carbon Absorption Prediction
- 🌱 Survival Probability Prediction
- 🌿 Tree Plantation Recommendation

---

# 🌍 Applications

- Smart City Planning
- Urban Forestry
- Municipal Corporations
- Environmental Monitoring
- Carbon Footprint Analysis
- Forest Management
- Climate Change Research
- Sustainable Development

---

# 🚀 Future Enhancements

- IoT Sensor Integration
- Weather API Integration
- GIS & GPS Mapping
- Satellite Image Analysis
- Deep Learning Models
- Mobile Application
- Explainable AI (XAI)
- Real-Time Monitoring
- Cloud Deployment

---

# 📸 Screenshots

```
images/
│
├── home.png
├── health_prediction.png
├── growth_prediction.png
├── carbon_prediction.png
├── survival_prediction.png
├── recommendation.png
└── dashboard.png
```

(Add screenshots after uploading.)

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## **Vipul Alsundkar**

**Software Testing Engineer | Data Analyst | Data Science & Machine Learning Enthusiast**

### Skills

- Python
- Machine Learning
- SQL
- Data Analytics
- Streamlit
- CatBoost
- XGBoost
- Power BI
- Tableau
- Selenium

**GitHub**

https://github.com/vipul892

**LinkedIn**

(Add your LinkedIn Profile)

**Email**

(Add your Email)

---

# ⭐ Support

If you found this project useful, don't forget to **⭐ Star** this repository.

It motivates me to build more Machine Learning and Data Science projects.

---

# 🙏 Acknowledgements

Special thanks to the open-source community and the developers of:

- Python
- Streamlit
- CatBoost
- XGBoost
- Scikit-learn
- Pandas
- NumPy
- Plotly
- Matplotlib

---

## 🌳 "Building Smarter Cities with Artificial Intelligence, Machine Learning, and Sustainable Urban Forestry."
