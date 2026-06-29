import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# =========================
# LOAD MODEL
# =========================
model = joblib.load("models\Tree_Health_Classification_Model.pkl")
feature_columns = joblib.load("models\Tree_Health_Prediction_Feature_Columns.pkl")
freq_maps = joblib.load("models/frequency_maps.pkl")
ordinal_encoder = joblib.load("models/ordinal_encoder.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

st.set_page_config(
    page_title="Tree Health Prediction Dashboard",
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
  

# set title    

st.title("🌳 Tree Health Prediction & Risk Assessment System")
st.markdown(
    """
    Input tree characteristics, environmental conditions, and stress-related factors to generate a health 
    prediction and support proactive tree management decisions...
    """
)

st.divider()


# =====================================
# INPUT FORM
# =====================================

col1, col2, col3 = st.columns(3)

# =====================================
# COLUMN 1 : TREE INFORMATION
# =====================================
with col1:

    st.markdown("""
    <h2 style="
    font-size:32px;
    font-weight:900;
    color:#1B5E20;
    ">
    🌳 Tree Information
    </h2>
    """, unsafe_allow_html=True)

    tree_name = st.selectbox(
        "🌲 Tree Species",
        sorted(df["Tree_Name"].dropna().unique())
    )

    root_condition = st.selectbox(
        "🌱 Root Condition",
        sorted(df["Root_Condition"].dropna().unique())
    )

    leaf_color = st.selectbox(
        "🍃 Leaf Color",
        sorted(df["Leaf_Color"].dropna().unique())
    )

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
# COLUMN 2 : ENVIRONMENT & SOIL
# =====================================
with col2:

    st.markdown("""
    <h2 style="
    font-size:32px;
    font-weight:900;
    color:#1B5E20;
    ">
    🌦️ Environment & Soil
    </h2>
    """, unsafe_allow_html=True)

    rainfall_mm = st.number_input(
        "🌧️ Rainfall (mm)",
        min_value=float(df["Rainfall_mm"].min()),
        max_value=float(df["Rainfall_mm"].max()),
        value=float(df["Rainfall_mm"].median())
    )

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


    organic_carbon = st.slider(
        "🌿 Organic Carbon (%)",
        min_value=float(df["Organic_Carbon"].min()),
        max_value=float(df["Organic_Carbon"].max()),
        value=float(df["Organic_Carbon"].median())
    )

    soil_ph = st.slider(
        "🧪 Soil pH",
        min_value=float(df["Soil_pH"].min()),
        max_value=float(df["Soil_pH"].max()),
        value=float(df["Soil_pH"].median())
    )


# =====================================
# COLUMN 3 : MAINTENANCE & CARE
# =====================================
with col3:

    st.markdown("""
    <h2 style="
    font-size:32px;
    font-weight:900;
    color:#1B5E20;
    ">
    🛠️ Maintenance & Care
    </h2>
    """, unsafe_allow_html=True)

    watering_frequency = st.selectbox(
        "🚰 Watering Frequency",
        sorted(df["Watering_Frequency"].dropna().unique())
    )

    pruning_count = st.number_input(
        "✂️ Pruning Count",
        min_value=int(df["Pruning_Count"].min()),
        max_value=int(df["Pruning_Count"].max()),
        value=int(df["Pruning_Count"].median())
    )

    treatment_history = st.selectbox(
        "💊 Treatment History",
        sorted(df["Treatment_History"].dropna().unique())
    )

    inspection_frequency = st.selectbox(
        "🔍 Inspection Frequency",
        sorted(df["Inspection_Frequency"].dropna().unique())
    )

st.markdown("---")

# =========================
# PREDICTION BUTTON
# =========================
if st.button("🔍 Predict Tree Health",use_container_width=True,type="primary"):


    
    input_df = pd.DataFrame([
        {
            "Tree_Name": tree_name,
            "Root_Condition": root_condition,
            "Leaf_Color": leaf_color,
            "Leaf_Drop_Percentage": leaf_drop_percentage,
            "Bark_Damage": bark_damage,
            "Organic_Carbon": organic_carbon,
            "Water_Stress_Index": water_stress_index,
            "Rainfall_mm": rainfall_mm,
            "Drought_Index": drought_index,
            "Pruning_Count": pruning_count,
            "Watering_Frequency": watering_frequency,
            "Treatment_History": treatment_history,
            "Inspection_Frequency": inspection_frequency,
            "Pest_Presence": pest_presence
        }
    ])


    # ----------------------
    # Encode using saved artifacts: frequency maps, ordinal encoder, label encoder
    # 1) Frequency map encoding (State_Province, City, Tree_Name)
    if isinstance(freq_maps, dict):
        for col, mapping in freq_maps.items():
            if col in input_df.columns:
                input_df[col] = input_df[col].map(mapping).fillna(0.0)

    # 2) Ordinal encoding using saved OrdinalEncoder categories
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
    if hasattr(ordinal_encoder, 'categories_'):
        for feature_name, categories in zip(ordinal_feature_names, ordinal_encoder.categories_):
            ordinal_maps[feature_name] = {category: float(idx) for idx, category in enumerate(categories)}

    for feat, mapping in ordinal_maps.items():
        if feat in input_df.columns:
            input_df[feat] = input_df[feat].map(mapping).fillna(0.0)

    # 3) Binary mapping for Yes/No columns
    binary_map = {"Yes": 1.0, "No": 0.0}
    for col in ["Pest_Presence", "Fungal_Infection"]:
        if col in input_df.columns:
            input_df[col] = input_df[col].map(binary_map).fillna(0.0)

    # 4) One-hot encode Soil_Type to match training columns
    if 'Soil_Type' in input_df.columns:
        soil_dummies = pd.get_dummies(input_df['Soil_Type'], prefix='Soil_Type', drop_first=True)
        input_df = input_df.drop(columns=['Soil_Type'])
        input_df = pd.concat([input_df, soil_dummies], axis=1)

    
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    

    # PREDICTION
   
    prediction = model.predict(input_df)[0] 

    # Decode label properly

    # decode predicted label using loaded label encoder
    health_status = label_encoder.inverse_transform([prediction])[0]


    confidence = None

    if hasattr(model, "predict_proba"):
        confidence = float(
            np.max(model.predict_proba(input_df)[0])
        )

    
    
# =====================================
# HEALTH STATUS MAPPING
# =====================================

    status = str(health_status).strip().lower()

    status_config = {
        "excellent": {
            "label": "Excellent",
            "color": "#00695C",
            "icon": "🏆",
            "message": "Tree is in excellent condition with optimal growth and minimal health risks."
        },
        "good": {
            "label": "Good",
            "color": "#2E7D32",
            "icon": "🌳",
            "message": "Tree is healthy and growing under favorable environmental conditions."
        },
        "fair": {
            "label": "Fair",
            "color": "#F9A825",
            "icon": "🌿",
            "message": "Tree condition is fair. Regular monitoring and preventive care are recommended."
        },
        "poor": {
            "label": "Poor",
            "color": "#C62828",
            "icon": "🚨",
            "message": "Tree health is poor and requires immediate attention."
        }
    }

    default_config = {
        "label": str(health_status),
        "color": "#616161",
        "icon": "❓",
        "message": "Unable to determine tree health status."
    }

    config = status_config.get(status, default_config)

    health_status = config["label"]
    color = config["color"]
    icon = config["icon"]
    message = config["message"]


   
    # MAIN LAYOUT
   
    left_col, right_col = st.columns([1, 1.5])

    
    # LEFT SIDE
 
    with left_col:


        st.markdown("## 🌳 Tree Health Result")


        st.markdown(
            f"""
            <div style="
                background:{color};
                padding:25px;
                border-radius:20px;
                color:white;
                text-align:center;
                box-shadow:0px 4px 15px rgba(0,0,0,0.2);
            ">
                <h1>{icon}</h1>
                <h2>{health_status}</h2>
                <p>{message}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### 🎯 Model Confidence")

        if confidence is not None:
            st.metric(
                "Confidence Score",
                f"{confidence*100:.1f}%"
            )




# =====================================
# RISK FACTORS ANALYSIS
# =====================================

        st.markdown("### ⚠️ Risk Factors Analysis")

        risk_factors = []

        # Root Condition
        if str(root_condition).lower() in [
            "poor",
            "damaged",
            "weak",
            "severely damaged"
        ]:
            risk_factors.append("🌱 Poor Root Condition")

        # Leaf Drop
        if leaf_drop_percentage > 50:
            risk_factors.append("🍂 Excessive Leaf Drop")

        # Bark Damage
        if str(bark_damage).lower() in [
            "high",
            "severe",
            "yes",
            "damaged"
        ]:
            risk_factors.append("🪵 Significant Bark Damage")

        # Water Stress
        if water_stress_index > 0.70:
            risk_factors.append("💧 High Water Stress")

        # Pest Presence
        if str(pest_presence).lower() == "yes":
            risk_factors.append("🐛 Pest Infestation Detected")

        # Organic Carbon
        if organic_carbon < 1.0:
            risk_factors.append("🌿 Low Soil Organic Carbon")

        # Pruning
        if pruning_count == 0:
            risk_factors.append("✂️ No Recent Pruning Activity")

        # Display Results
        if risk_factors:

            for risk in risk_factors:
                st.warning(risk)

        else:
            st.success("✅ No significant risk factors detected.")
   
        st.markdown("</div>", unsafe_allow_html=True)
    
    # ====================================================
    # RIGHT SIDE
    # ====================================================
    with right_col:


        st.markdown("## 📊 Feature Importance Analysis")

        if hasattr(model, "feature_importances_"):

            import plotly.express as px

            importance_df = pd.DataFrame({
                "Feature": feature_columns,
                "Importance": model.feature_importances_
            })

            importance_df = (
                importance_df
                .sort_values("Importance", ascending=False)
                .head(5)
                .sort_values("Importance")
            )

            fig = px.bar(
                importance_df,
                x="Importance",
                y="Feature",
                orientation="h",
                text="Importance",
                title="Top 10 Influential Features"
            )

            fig.update_traces(
                texttemplate="%{text:.3f}",
                textposition="outside"
            )

            fig.update_layout(
                height=550,
                showlegend=False,
                plot_bgcolor="white",
                paper_bgcolor="white",
                xaxis_title="Importance Score",
                yaxis_title="",
                margin=dict(
                    l=20,
                    r=20,
                    t=50,
                    b=20
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

         

# =====================================
# INTELLIGENT RECOMMENDATIONS
# =====================================

    st.markdown("---")
    st.subheader("💡 Intelligent Tree Care Recommendations")

    if status == "poor":

        recommendation_color = "#ffebee"
        border_color = "#C62828"

        recommendation_html = """
        <h3>🚨 Critical Tree Health Alert</h3>

        <h4>🔴 Recommended Actions</h4>

        <p>
        🔍 Inspect roots, trunk, and foliage immediately<br>
        🐛 Check for pest infestation<br>
        🍄 Check for fungal infection<br>
        💧 Improve watering practices<br>
        🌱 Improve soil quality and nutrient availability<br>
        👨‍🌾 Consult an arborist if symptoms persist
        </p>

        <h4>📅 Monitoring Schedule</h4>
        <p>📍 Inspect every 7 days</p>
        """

    elif status == "fair":

        recommendation_color = "#fff8e1"
        border_color = "#F9A825"

        recommendation_html = """
        <h3>⚠️ Moderate Health Condition</h3>

        <h4>🟡 Recommended Actions</h4>

        <p>
        💧 Monitor water stress regularly<br>
        🐛 Check for early pest activity<br>
        🌱 Maintain adequate soil moisture<br>
        ✂️ Perform preventive pruning if required<br>
        🔍 Conduct regular inspections
        </p>

        <h4>📅 Monitoring Schedule</h4>
        <p>📍 Inspect every 2–4 weeks</p>
        """

    elif status == "good":

        recommendation_color = "#f1f8e9"
        border_color = "#2E7D32"

        recommendation_html = """
        <h3>🌳 Healthy Tree Condition</h3>

        <h4>🟢 Recommended Actions</h4>

        <p>
        💧 Continue current watering schedule<br>
        🌱 Maintain soil fertility<br>
        ✂️ Perform routine pruning<br>
        🔍 Conduct seasonal inspections<br>
        🌤️ Monitor environmental changes
        </p>

        <h4>📅 Monitoring Schedule</h4>
        <p>📍 Inspect every month</p>
        """

    elif status == "excellent":

        recommendation_color = "#e8f5e9"
        border_color = "#00695C"

        recommendation_html = """
        <h3>🏆 Excellent Tree Health</h3>

        <h4>🌟 Best Practices</h4>

        <p>
        💧 Maintain current irrigation practices<br>
        🌱 Preserve soil organic matter<br>
        🌿 Continue sustainable maintenance<br>
        🔍 Perform preventive inspections<br>
        🌳 Protect surrounding biodiversity
        </p>

        <h4>📅 Monitoring Schedule</h4>
        <p>📍 Routine inspection every 2 months</p>
        """

    st.markdown(
        f"""
        <div style="
            background-color:{recommendation_color};
            padding:20px;
            border-radius:15px;
            border-left:6px solid {border_color};
            box-shadow:0px 4px 12px rgba(0,0,0,0.15);
            margin-bottom:15px;
        ">
            {recommendation_html}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("""
---
<div style='text-align:center; color:green;'>
<h4>🌳 Tree Health Prediction & Risk Assessment System</h4>
<p>Empowering Sustainable Tree Management Through Machine Learning and Predictive Analytics</p>
</div>
""", unsafe_allow_html=True)