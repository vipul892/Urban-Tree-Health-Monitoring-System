import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go


# ======================
# LOAD MODELS
# ======================
carbon_model = joblib.load("models/Carbon_Prediction_Model.pkl")
carbon_features = joblib.load("models/Carbon_Prediction_Feature_Columns.pkl")
freq_maps = joblib.load("models/frequency_maps.pkl")
ordinal_encoder = joblib.load("models/ordinal_encoder.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")


# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="🌳 Carbon Sequestration Predictor",
    layout="wide"
)

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

/* Number Input Labels */
.stNumberInput label {
    font-size: 22px !important;
    font-weight: 900 !important;
    color: black !important;
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

.section-title{
    font-size:22px;
    font-weight:bold;
    color:#145A32;
    margin-bottom:10px;
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

  
# =====================================
# TITLE
# =====================================
st.title("🌳 Smart Carbon Sequestration Predictor")

st.markdown("""
Estimate the carbon capture and storage potential of urban trees using advanced Machine Learning models.

""")

st.divider()

# =====================================
# INPUT SECTION
# =====================================
st.markdown("""
<div class='section-title'>
🌳 Carbon Sequestration Input Panel
</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:

    tree_name = st.selectbox(
        "🌲 Tree Species",
        sorted(df["Tree_Name"].dropna().unique())
    )


    tree_age = st.number_input(
        "🌳 Tree Age (Years)",
        min_value=int(df["Tree_Age"].min()),
        max_value=int(df["Tree_Age"].max()),
        value=int(df["Tree_Age"].median())
    )

    height = st.slider(
        "📏 Height (m)",
        min_value=float(df["Height_Meter"].min()),
        max_value=float(df["Height_Meter"].max()),
        value=float(df["Height_Meter"].median())
    )

    trunk_diameter = st.slider(
        "🌲 Trunk Diameter (cm)",
        min_value=float(df["Trunk_Diameter_cm"].min()),
        max_value=float(df["Trunk_Diameter_cm"].max()),
        value=float(df["Trunk_Diameter_cm"].median())
    )

    canopy_width = st.slider(
        "🍃 Canopy Width (m)",
        min_value=float(df["Canopy_Width_m"].min()),
        max_value=float(df["Canopy_Width_m"].max()),
        value=float(df["Canopy_Width_m"].median())
    )

with col2:

    root_depth = st.slider(
        "🌱 Root Depth (m)",
        min_value=float(df["Root_Depth_m"].min()),
        max_value=float(df["Root_Depth_m"].max()),
        value=float(df["Root_Depth_m"].median())
    )

    water_stress = st.slider(
        "💧 Water Stress Index",
        min_value=float(df["Water_Stress_Index"].min()),
        max_value=float(df["Water_Stress_Index"].max()),
        value=float(df["Water_Stress_Index"].median())
    )

    pest_presence = st.selectbox(
        "🐛 Pest Presence",
        sorted(df["Pest_Presence"].dropna().unique())
    )

    bark_damage = st.selectbox(
        "🪵 Bark Damage",
        sorted(df["Bark_Damage"].dropna().unique())
    )

# =====================================
# PREDICTION
# =====================================
if st.button("🚀 Predict Carbon Sequestration", use_container_width=True,type="primary"):

    input_data = pd.DataFrame({
        "Tree_Name": [tree_name],
        "Tree_Age": [tree_age],
        "Height_Meter": [height],
        "Trunk_Diameter_cm": [trunk_diameter],
        "Canopy_Width_m": [canopy_width],
        "Root_Depth_m": [root_depth],
        "Water_Stress_Index": [water_stress],
        "Pest_Presence": [pest_presence],
        "Bark_Damage": [bark_damage]
    })

    # Use saved artifacts for encoding
    if isinstance(freq_maps, dict):
        for col, mapping in freq_maps.items():
            if col in input_data.columns:
                input_data[col] = input_data[col].map(mapping).fillna(0.0)

    if hasattr(ordinal_encoder, 'categories_'):
        ordinal_feature_names = [
            "Growth_Stage",
            "Leaf_Color",
            "Disease_Symptoms",
            "Bark_Damage",
            "Root_Condition",
            "Watering_Frequency",
            "Fertilizer_Usage",
            "Treatment_History",
            "Inspection_Frequency"
        ]
        ordinal_maps = {}
        for feature_name, categories in zip(ordinal_feature_names, ordinal_encoder.categories_):
            ordinal_maps[feature_name] = {category: float(idx) for idx, category in enumerate(categories)}

        for feat, mapping in ordinal_maps.items():
            if feat in input_data.columns:
                input_data[feat] = input_data[feat].map(mapping).fillna(0.0)

    binary_map = {"Yes": 1.0, "No": 0.0}
    for col in ["Pest_Presence", "Fungal_Infection"]:
        if col in input_data.columns:
            input_data[col] = input_data[col].map(binary_map).fillna(0.0)

    if 'Soil_Type' in input_data.columns:
        soil_dummies = pd.get_dummies(input_data['Soil_Type'], prefix='Soil_Type', drop_first=True)
        input_data = input_data.drop(columns=['Soil_Type'])
        input_data = pd.concat([input_data, soil_dummies], axis=1)

    # Match model feature order and fill missing features
    for col in carbon_features:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[carbon_features]

    prediction = float(carbon_model.predict(input_data)[0])

# =====================================
# RESULTS DASHBOARD
# =====================================

    st.markdown("## 🌍 Carbon Sequestration Analysis")

    # -----------------------------
    # CALCULATIONS
    # -----------------------------
    oxygen_generated = prediction * 2.67
    cars_offset = prediction / 4600

    # -----------------------------
    # KPI CARDS
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#00c853,#64dd17);
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
            box-shadow:0 4px 10px rgba(0,0,0,0.2);">
            <h4>🌳 Carbon Stored</h4>
            <h2>{prediction:.2f} kg</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#0288d1,#26c6da);
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
            box-shadow:0 4px 10px rgba(0,0,0,0.2);">
            <h4>🌬 Oxygen Generated</h4>
            <h2>{oxygen_generated:.2f} kg</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#ff6f00,#ffca28);
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
            box-shadow:0 4px 10px rgba(0,0,0,0.2);">
            <h4>🚗 Cars Offset</h4>
            <h2>{cars_offset:.4f}</h2>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==============================
    # CARBON CATEGORY
    # ==============================

    if prediction < 55:
        category = "🔴 Low Carbon Storage"
        color = "#e53935"

    elif prediction < 70:
        category = "🟡 Moderate Carbon Storage"
        color = "#fbc02d"

    elif prediction < 80:
        category = "🟢 High Carbon Storage"
        color = "#43a047"

    else:
        category = "🌟 Excellent Carbon Sink"
        color = "#1b5e20"

    st.markdown(f"""
    <div style="
        background:{color};
        padding:15px;
        border-radius:12px;
        text-align:center;
        color:white;
        font-size:22px;
        font-weight:bold;
        margin-top:10px;
        margin-bottom:20px;">
        {category}
    </div>
    """, unsafe_allow_html=True)

    # ==============================
    # CHART SECTION
    # ==============================
    col1, col2 = st.columns(2)

    # =====================================
    # GAUGE CHART (FIXED RANGE)
    # =====================================
    with col1:

        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prediction,
            title={"text": "🌳 Carbon Sequestration (kg)"},
            gauge={
                "axis": {"range": [0, 100]},  # based on dataset max = 88
                "bar": {"color": "darkgreen"},
                "steps": [
                    {"range": [0, 55], "color": "#ffcdd2"},
                    {"range": [55, 70], "color": "#fff9c4"},
                    {"range": [70, 80], "color": "#c8e6c9"},
                    {"range": [80, 100], "color": "#81c784"}
                ]
            }
        ))

        gauge.update_layout(
            height=400,
            margin=dict(l=20, r=20, t=40, b=20)
        )

        st.plotly_chart(gauge, use_container_width=True)

    # =====================================
    # TREE STRUCTURE COMPARISON
    # =====================================
    with col2:

        tree_profile = go.Figure()

        tree_profile.add_trace(go.Bar(
            x=[
                "Height (m)",
                "Trunk Diameter (cm)",
                "Canopy Width (m)",
                "Root Depth (m)"
            ],
            y=[
                height,
                trunk_diameter,
                canopy_width,
                root_depth
            ],
            text=[
                round(height, 2),
                round(trunk_diameter, 2),
                round(canopy_width, 2),
                round(root_depth, 2)
            ],
            textposition="outside",
            marker_color="#2e7d32"
        ))

        tree_profile.update_layout(
            title="🌳 Tree Biomass Structure",
            height=400,
            template="plotly_white",
            showlegend=False,
            xaxis_title="Features",
            yaxis_title="Value"
        )

        st.plotly_chart(tree_profile, use_container_width=True)

    # ==============================
    # IMPACT SUMMARY
    # ==============================
    st.markdown("## 🌱 Environmental Impact Summary")

    st.markdown(f"""
    <div style="
        background:#e8f5e9;
        padding:20px;
        border-radius:15px;
        border-left:8px solid #2e7d32;
        font-size:16px;">

    ### 🌍 Prediction Result

    ✔ Predicted Carbon Storage: <b>{prediction:.2f} kg</b><br>
    ✔ Estimated Oxygen Contribution: <b>{oxygen_generated:.2f} kg</b><br>
    ✔ Carbon Offset Equivalent: <b>{cars_offset:.4f} vehicles</b><br>

    </div>
    """, unsafe_allow_html=True)

    # -----------------------------
    # FOOTER
    # -----------------------------
st.markdown("""
---
<div style='text-align:center; color:green;'>
<h4>🌿 Smart Carbon Sequestration Predictor</h4>
<p>Supporting Climate Action Through Machine Learning and Urban Forest Carbon Intelligence</p>
</div>
""", unsafe_allow_html=True)