import streamlit as st
import numpy as np
import pandas as pd
import joblib
import plotly.graph_objects as go

# =========================
# LOAD MODEL & SUPPORT FILES
# =========================
survial_model = joblib.load("models\Survival_Prediction_Model.pkl")
feature_columns = joblib.load("models\Survival_feature_columns.pkl")
freq_maps = joblib.load("models/frequency_maps.pkl")
ordinal_encoder = joblib.load("models/ordinal_encoder.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Tree Survival Prediction", layout="wide")

st.title("🌳 Tree Survival Prediction")
st.markdown("Predict survival probability of urban trees using ML model.")



@st.cache_data
def load_data():
    return pd.read_csv("data/raw_data/trees_indian_dataset.csv")

df = load_data()

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>
/* Main App */
.stApp{
    background-color:#f5f7f5;
}

/* Sidebar Background */
[data-testid="stSidebar"]{
    background: linear-gradient(    
        180deg,
        #022c22 0%,
        #0b5d3b 50%,
        #198754 100%
    );
}
/* Logo Section */
.logo-container{
    text-align:center;
    margin:0;
    padding:0;
}

.logo-container h2{
    color:white;
    font-size:20px;
    font-weight:700;
    margin:8px 0 3px 0;
    line-height:1.2;
}

.logo-container p{
    color:#d8f3dc;
    font-size:13px;
    margin:0;
    line-height:1.2;
}

/* Hide Streamlit Navigation */
[data-testid="stSidebarNav"]{
    display:none;
}

[data-testid="stSidebarHeader"]{
    display:none;
}

/* Navigation Buttons */
[data-testid="stSidebar"] .stPageLink a{
    background: rgba(255,255,255,0.08);
    padding:10px 12px;
    border-radius:12px;
    margin-bottom:8px;
    transition:0.3s;
    font-weight:500;
}

[data-testid="stSidebar"] .stPageLink a:hover{
    background:#2d6a4f;
    transform:translateX(5px);
}

/* Active Page */
[data-testid="stSidebar"] .stPageLink a[aria-current="page"]{
    background:#40916c;
    border-left:4px solid #d8f3dc;
}

/* Footer */
.sidebar-footer{
    text-align:center;
    color:#d8f3dc;
    font-size:12px;
    padding-top:15px;
}                         

/* Sidebar Text */
[data-testid="stSidebar"] *{
    color:white;
}

/* Project Title */
.sidebar-title{
    text-align:center;
    font-size:15px;
    font-weight:bold;
    color:white;
}

.sidebar-subtitle{
    text-align:center;
    color:#c8f7c5;
    font-size:13px;
}

/* Header */
.main-title{
    color:#145A32;
    font-size:25px;
    font-weight:bold;
}
            
.input-card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 4px 20px rgba(0,0,0,0.12);
    margin-bottom:20px;
}

.section-title{
    font-size:22px;
    font-weight:bold;
    color:#145A32;
    margin-bottom:10px;
}

/* Text Input Labels */
.stTextInput label {
    font-size: 22px !important;
    font-weight: 900 !important;
    color: black !important;
}

/* Selectbox Labels */
.stSelectbox label {
    font-size: 22px !important;
    font-weight: 900 !important;
    color: black !important;
}

/* Multiselect Labels */
.stMultiSelect label {
    font-size: 22px !important;
    font-weight: 900 !important;
    color: black !important;
}

/* Slider Labels */
.stSlider label {
    font-size: 22px !important;
    font-weight: 900 !important;
    color: black !important;
}

/* Radio Labels */
.stRadio label {
    font-size: 22px !important;
    font-weight: 900 !important;
    color: black !important;
}                      
            
/* Hide Streamlit Branding */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}
            
</style>
""", unsafe_allow_html=True)                        

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    # Center Logo
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.image("images/logo.png", width=400)

    # Title & Subtitle
    st.markdown("""
    <div style="text-align:center;">

    <h2 style="
        color:white;
        font-size:20px;
        font-weight:700;
        margin-bottom:5px;">
        🌳 Urban Tree Health
    </h2>

    <p style="
        color:#d8f3dc;
        font-size:14px;
        margin-top:0px;">
        Monitoring & Recommendation System
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Navigation
    st.page_link("Home.py", label="🏠 Home")
    st.page_link("pages/1_Health_Prediction.py", label="💚 Health Prediction")
    st.page_link("pages/2_Growth_Prediction.py", label="📈 Growth Prediction")
    st.page_link("pages/3_Carbon_Prediction.py", label="🌍 Carbon Prediction")
    st.page_link("pages/4_Survival_Prediction.py", label="🌱 Survival Prediction")
    st.page_link("pages/5_Tree_Recommendation.py", label="🌳 Tree Recommendation")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-footer">
        🌿 Sustainable Urban Forestry
    </div>
    """, unsafe_allow_html=True)
  

# =========================
# INPUT PANEL
# =========================

st.markdown("""
<div class='section-title'>
🌳 Tree Survival Input Panel
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs([
    "🌳 Tree Characteristics",
    "🌦️ Environmental Factors",
    "🛠️ Maintenance Factors"
])

# =====================================
# TAB 1 : TREE CHARACTERISTICS
# =====================================

with tab1:

    col1, col2 = st.columns(2)

    with col1:

        tree_name = st.selectbox(
            "🌲 Tree Species",
            sorted(df["Tree_Name"].dropna().unique())
        )

        leaf_color = st.selectbox(
            "🍃 Leaf Color",
            sorted(df["Leaf_Color"].dropna().unique())
        )

        root_condition = st.selectbox(
            "🌱 Root Condition",
            sorted(df["Root_Condition"].dropna().unique())
        )

    with col2:

        leaf_drop_percentage = st.slider(
            "🍂 Leaf Drop Percentage (%)",
            min_value=int(df["Leaf_Drop_Percentage"].min()),
            max_value=int(df["Leaf_Drop_Percentage"].max()),
            value=int(df["Leaf_Drop_Percentage"].median())
        )

        bark_damage = st.selectbox(
            "🪵 Bark Damage",
            sorted(df["Bark_Damage"].dropna().unique())
        )

        pest_presence = st.selectbox(
            "🐛 Pest Presence",
            sorted(df["Pest_Presence"].dropna().unique())
        )

# =====================================
# TAB 2 : ENVIRONMENTAL STRESS
# =====================================

with tab2:

    col1, col2 = st.columns(2)

    with col1:

        water_stress_index = st.slider(
            "💧 Water Stress Index",
            min_value=float(df["Water_Stress_Index"].min()),
            max_value=float(df["Water_Stress_Index"].max()),
            value=float(df["Water_Stress_Index"].median())
        )

        drought_index = st.slider(
            "🌵 Drought Index",
            min_value=float(df["Drought_Index"].min()),
            max_value=float(df["Drought_Index"].max()),
            value=float(df["Drought_Index"].median())
        )

    with col2:

        organic_carbon = st.number_input(
            "🌿 Organic Carbon (%)",
            min_value=float(df["Organic_Carbon"].min()),
            max_value=float(df["Organic_Carbon"].max()),
            value=float(df["Organic_Carbon"].median())
        )

# =====================================
# TAB 3 : MAINTENANCE FACTORS
# =====================================

with tab3:

    col1, col2 = st.columns(2)

    with col1:

        inspection_frequency = st.selectbox(
            "🔍 Inspection Frequency",
            sorted(df["Inspection_Frequency"].dropna().unique())
        )

        treatment_history = st.selectbox(
            "💊 Treatment History",
            sorted(df["Treatment_History"].dropna().unique())
        )

    with col2:

        watering_frequency = st.selectbox(
            "🚰 Watering Frequency",
            sorted(df["Watering_Frequency"].dropna().unique())
        )

        fertilizer_usage = st.selectbox(
            "🧪 Fertilizer Usage",
            sorted(df["Fertilizer_Usage"].dropna().unique())
        )

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# PREDICTION
# =========================
if st.button("🌱 Predict Survival Probability", use_container_width=True,type="primary"):

# =========================
# DATA PREPARATION
# =========================

    input_data = {
    "Tree_Name": tree_name,
    "Leaf_Color": leaf_color,
    "Leaf_Drop_Percentage": leaf_drop_percentage,
    "Pest_Presence": pest_presence,
    "Bark_Damage": bark_damage,
    "Root_Condition": root_condition,
    "Water_Stress_Index": water_stress_index,
    "Drought_Index": drought_index,
    "Organic_Carbon": organic_carbon,
    "Inspection_Frequency": inspection_frequency,
    "Treatment_History": treatment_history,
    "Watering_Frequency": watering_frequency,
    "Fertilizer_Usage": fertilizer_usage
}

    input_df = pd.DataFrame([input_data])

    # ENCODING ALIGNMENT USING SAVED PKL ARTIFACTS
    if isinstance(freq_maps, dict):
        for col, mapping in freq_maps.items():
            if col in input_df.columns:
                input_df[col] = input_df[col].map(mapping).fillna(0.0)

    ordinal_feature_names = [
        "Root_Condition",
        "Leaf_Color",
        "Bark_Damage",
        "Inspection_Frequency",
        "Treatment_History",
        "Watering_Frequency",
        "Fertilizer_Usage"
    ]
    ordinal_maps = {}
    if hasattr(ordinal_encoder, 'categories_'):
        for feature_name, categories in zip(ordinal_feature_names, ordinal_encoder.categories_):
            ordinal_maps[feature_name] = {category: float(idx) for idx, category in enumerate(categories)}

    for col, mapping in ordinal_maps.items():
        if col in input_df.columns:
            input_df[col] = input_df[col].map(mapping).fillna(0.0)

    binary_map = {"Yes": 1.0, "No": 0.0}
    if 'Pest_Presence' in input_df.columns:
        input_df['Pest_Presence'] = input_df['Pest_Presence'].map(binary_map).fillna(0.0)

    if 'Soil_Type' in input_df.columns:
        soil_dummies = pd.get_dummies(input_df['Soil_Type'], prefix='Soil_Type', drop_first=True)
        input_df = input_df.drop(columns=['Soil_Type'])
        input_df = pd.concat([input_df, soil_dummies], axis=1)

    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    prediction = survial_model.predict(input_df)[0]  # survival class probability


# =========================
# RESULT SECTION
# =========================

    survival_percent = prediction * 100

    st.markdown("---")
    st.subheader("📊 Survival Prediction Results")

    # =========================
    # RISK STATUS CARD
    # =========================

    if prediction >= 0.75:
        risk_color = "#28a745"
        risk_status = "🟢 High Survival Chance"
    elif prediction >= 0.45:
        risk_color = "#ff9800"
        risk_status = "🟠 Moderate Survival Chance"
    else:
        risk_color = "#dc3545"
        risk_status = "🔴 Low Survival Chance"

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:15px;
            background-color:{risk_color};
            color:white;
            text-align:center;
            font-size:24px;
            font-weight:bold;
            margin-bottom:20px;">
            {risk_status}
            <br><br>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # GAUGE CHART
    # =========================

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=survival_percent,
        number={"suffix": "%"},
        title={"text": "🌳 Tree Survival Probability"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "darkgreen"},
            "steps": [
                {"range": [0, 45], "color": "#ff4d4d"},
                {"range": [45, 75], "color": "#ffa500"},
                {"range": [75, 100], "color": "#66cc66"}
            ]
        }
    ))

    fig.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=60, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

    # =========================
    # RECOMMENDATION CARD
    # =========================

    st.markdown("### 💡 Recommendation")

    if prediction >= 0.75:
        st.success("""
    🌳 Tree condition is excellent.

    ✅ Continue current maintenance practices.

    ✅ Monitor tree health regularly.

    ✅ Ensure adequate watering and soil care.
    """)

    elif prediction >= 0.45:
        st.warning("""
    ⚠️ Tree requires attention.

    🔍 Inspect for pests and diseases.

    💧 Improve irrigation schedule.

    🌦️ Monitor environmental stress factors.
    """)

    else:
        st.error("""
    🚨 Tree is at high survival risk.

    🔴 Immediate inspection recommended.

    🐛 Treat pests and diseases urgently.

    🌱 Improve soil quality and water availability.

    👨‍🌾 Consider expert arborist assessment.
    """)

st.markdown("""
---
<div style='text-align:center; color:green;'>
<h4>🌳 Tree Survival Prediction Dashboard</h4>
<p>Predicting Tree Survival for Sustainable Urban Forest Management</p>
</div>
""", unsafe_allow_html=True)        