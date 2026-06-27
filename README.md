# 🌳 Urban Tree Health Monitoring & Smart Plantation Recommendation System

> **An End-to-End Machine Learning Project** for predicting **Tree Health**, **Tree Growth**, **Carbon Absorption**, and **Tree Survival Probability**, along with an intelligent **Plantation Recommendation System** to support sustainable urban forestry and smart city planning.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![CatBoost](https://img.shields.io/badge/CatBoost-ML_Model-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

---

# 📖 Table of Contents

- Project Overview
- Problem Statement
- Objectives
- Features
- Machine Learning Models
- Dataset
- Exploratory Data Analysis
- Data Preprocessing
- Model Training
- Model Evaluation
- Technology Stack
- Project Structure
- Installation
- Running the Application
- Screenshots
- Applications
- Future Scope
- Contributing
- License
- Author

---

# 🌍 Project Overview

Urban trees improve air quality, reduce pollution, lower urban temperatures, absorb carbon dioxide, and enhance biodiversity. However, monitoring tree health manually is difficult, expensive, and time-consuming.

This project uses **Machine Learning** to automate urban tree analysis by predicting:

- 🌳 Tree Health Status
- 📈 Tree Growth
- 🌍 Carbon Absorption
- 🌱 Tree Survival Probability

Additionally, the system recommends the most suitable tree species for plantation based on environmental conditions.

The application is developed using **Python**, **CatBoost**, and **Streamlit**, providing an interactive and user-friendly interface.

---

# ❗ Problem Statement

Urban authorities and environmental organizations often struggle with:

- Manual tree health inspections
- Poor plantation planning
- Lack of predictive analysis
- Inefficient resource allocation
- Limited environmental monitoring

This project addresses these challenges through intelligent Machine Learning models.

---

# 🎯 Project Objectives

- Predict urban tree health.
- Estimate future tree growth.
- Calculate annual carbon absorption.
- Predict survival probability.
- Recommend suitable tree species.
- Visualize urban forestry data.
- Support sustainable urban development.

---

# 🚀 Features

## 🌳 Tree Health Prediction

Predicts whether a tree is:

- Healthy
- Moderate
- Unhealthy

**Algorithm:** CatBoost Classifier

---

## 📈 Tree Growth Prediction

Predicts future growth using environmental and biological features.

Outputs include:

- Height
- Trunk Diameter
- Canopy Width
- Root Growth

**Algorithm:** CatBoost Regressor

---

## 🌍 Carbon Absorption Prediction

Predicts annual carbon dioxide absorption.

Outputs:

- Carbon Absorption (kg/year)
- Environmental Contribution

**Algorithm:** CatBoost Regressor

---

## 🌱 Tree Survival Probability Prediction

Predicts survival percentage under current environmental conditions.

Outputs:

- Survival Probability
- Risk Category

**Algorithm:** CatBoost Classifier

---

## 🌿 Plantation Recommendation System

Recommends suitable tree species based on:

- Temperature
- Soil Moisture
- Rainfall
- Pollution Level
- Root Depth
- Available Space
- Sunlight
- Climate

---

# 📂 Dataset Features

## 🌳 Tree Information

- Tree Name
- Tree Age
- Species
- Height
- Trunk Diameter
- Canopy Width
- Root Depth

---

## 🌿 Biological Features

- Leaf Color
- Root Condition
- Disease Symptoms
- Pest Presence

---

## 🌍 Environmental Features

- Temperature
- Humidity
- Rainfall
- Soil Moisture
- Wind Speed
- Air Pollution
- Sunlight Exposure

---

## 🎯 Target Variables

- Health Status
- Growth
- Carbon Absorption
- Survival Probability

---

# 📊 Exploratory Data Analysis (EDA)

The project includes:

- Missing Value Analysis
- Feature Distribution
- Correlation Heatmap
- Outlier Detection
- Feature Importance
- Statistical Summary
- Target Distribution

---

# ⚙ Data Preprocessing

The dataset undergoes:

- Missing Value Handling
- Label Encoding
- Feature Engineering
- Feature Scaling (where applicable)
- Train-Test Split

---

# 🤖 Machine Learning Models

| Module | Model |
|---------|-------|
| Tree Health Prediction | CatBoost Classifier |
| Tree Growth Prediction | CatBoost Regressor |
| Carbon Absorption Prediction | CatBoost Regressor |
| Survival Probability Prediction | CatBoost Classifier |
| Recommendation System | Rule-Based Recommendation |

---

# 📈 Model Evaluation

## Classification Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Regression Metrics

- R² Score
- MAE
- MSE
- RMSE

---

# 💻 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Streamlit | Web Application |
| Pandas | Data Analysis |
| NumPy | Numerical Computing |
| Scikit-learn | Preprocessing & Evaluation |
| CatBoost | Machine Learning |
| Plotly | Interactive Visualization |
| Matplotlib | Charts |
| Joblib | Model Saving |

---

# 📁 Project Structure

```
Urban-Tree-Health-Monitoring-System
│
├── dataset/
│   ├── urban_tree_dataset.csv
│
├── models/
│   ├── health_model.pkl
│   ├── growth_model.pkl
│   ├── carbon_model.pkl
│   ├── survival_model.pkl
│   └── label_encoders.pkl
│
├── notebooks/
│   └── EDA.ipynb
│
├── recommendation/
│   └── recommendation.py
│
├── images/
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🔄 Machine Learning Workflow

```
Data Collection
       │
       ▼
Data Cleaning
       │
       ▼
EDA
       │
       ▼
Feature Engineering
       │
       ▼
Preprocessing
       │
       ▼
Train/Test Split
       │
       ▼
Model Training
       │
       ▼
Model Evaluation
       │
       ▼
Model Saving
       │
       ▼
Streamlit Deployment
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/vipul892/Urban-Tree-Health-Monitoring-System.git
```

Move to project directory

```bash
cd Urban-Tree-Health-Monitoring-System
```

Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run Application

```bash
streamlit run app.py
```

Open browser

```
http://localhost:8501
```

---

# 📸 Application Screenshots

## 🏠 Home Page

> Add screenshot here

---

## 🌳 Tree Health Prediction

> Add screenshot here

---

## 📈 Tree Growth Prediction

> Add screenshot here

---

## 🌍 Carbon Absorption Prediction

> Add screenshot here

---

## 🌱 Survival Probability Prediction

> Add screenshot here

---

## 🌿 Plantation Recommendation

> Add screenshot here

---

## 📊 Dashboard

> Add screenshot here

---

# 🌍 Applications

- Urban Forestry Management
- Smart Cities
- Municipal Corporations
- Environmental Monitoring
- Climate Change Research
- Carbon Footprint Analysis
- Government Forestry Departments
- Academic Research
- Sustainable Development Projects

---

# 🚀 Future Scope

- 🌐 IoT Sensor Integration
- 📍 GPS Tree Mapping
- 🛰 GIS Integration
- 🌦 Weather API
- ☁ Cloud Deployment
- 🤖 Deep Learning Models
- 📱 Android & iOS Application
- 🌍 Satellite Image Analysis
- 📈 Real-Time Monitoring
- 🧠 Explainable AI (XAI)

---

# 🤝 Contributing

Contributions are welcome.

1. Fork this repository.
2. Create your feature branch.

```bash
git checkout -b feature-name
```

3. Commit changes.

```bash
git commit -m "Add new feature"
```

4. Push to GitHub.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Vipul Alsundkar

**Software Testing Engineer | Data Analyst | Data Scientist | Machine Learning Enthusiast**

### Skills

- Python
- Machine Learning
- SQL
- Data Analytics
- Streamlit
- Power BI
- Tableau
- Selenium
- MySQL

**GitHub**

https://github.com/vipul892

**LinkedIn**

Add your LinkedIn profile

**Email**

Add your email address

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ **Star** on GitHub.

Your support motivates future improvements and the development of more open-source Machine Learning projects.

---

# 💚 Acknowledgements

Special thanks to the open-source community and the developers of:

- Python
- Streamlit
- CatBoost
- Scikit-learn
- Pandas
- NumPy
- Plotly
- Matplotlib

---

## 🌳 *"Empowering Sustainable Urban Forestry through Artificial Intelligence and Machine Learning."*
