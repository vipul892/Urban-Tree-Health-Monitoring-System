import streamlit as st
import pandas as pd
import joblib

import plotly.graph_objects as go
import plotly.express as px

# ======================
# LOAD MODELS
# ======================
growth_model = joblib.load("models/Growth_Prediction_Model.pkl")
growth_features = joblib.load("models/Growth_feature_columns.pkl")
freq_maps = joblib.load("models/frequency_maps.pkl")
ordinal_encoder = joblib.load("models/ordinal_encoder.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")


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
if hasattr(ordinal_encoder, "categories_"):
    for feature_name, categories in zip(ordinal_feature_names, ordinal_encoder.categories_):
        ordinal_maps[feature_name] = {category: float(index) for index, category in enumerate(categories)}

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Tree Growth Prediction",
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
            
.metric-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    text-align:center;
    margin-bottom:15px;
}

.chart-card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    margin-top:15px;
}

.title-card {
    background: linear-gradient(135deg,#2E7D32,#43A047);
    color:white;
    padding:20px;
    border-radius:20px;
    text-align:center;
    margin-bottom:25px;
    box-shadow:0px 6px 20px rgba(0,0,0,0.15);
}
            
.chart-container{
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
    border: 1px solid #e5e7eb;
    margin-bottom: 15px;
}            

/* KPI Cards */
..metric-card{
    background: white;
    height: 180px;                
    width: 100%;               
    border-radius: 18px;
    border: 1px solid #e5e7eb;

    box-shadow: 0 8px 20px rgba(0,0,0,0.08);

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    padding: 20px;
    text-align: center;

    transition: 0.3s ease;
}

.metric-card:hover{
    transform: translateY(-3px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.12);
}

.metric-card h3{
    margin: 0;
    font-size: 18px;
    color: #555;
}

.metric-card h2{
    margin: 12px 0;
    font-size: 38px;
    font-weight: bold;
    color: #145A32;
}

.metric-card p{
    margin: 0;
    color: #777;
    font-size: 14px;
}

/* Insight Card */
.insight-card{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0 8px 24px rgba(0,0,0,0.08);
    border-left:5px solid #2E7D32;
}

/* Plotly Charts */
div[data-testid="stPlotlyChart"]{
    background:white;
    padding:15px;
    border-radius:18px;
    box-shadow:0 8px 24px rgba(0,0,0,0.08);
    border:1px solid #e5e7eb;
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


# set Title

st.title("🌳 Tree Growth Prediction System")
st.markdown("Predict Growth Performance Using Tree Attributes, Climate, and Soil Conditions")

st.divider()    

# input section title

st.markdown("""
<div class='section-title'>
🌳 Tree Growth Input Panel
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# =====================================
# COLUMN 1
# =====================================
with col1:

    tree_name = st.selectbox(
        "🌳 Tree Name",
        sorted(df["Tree_Name"].dropna().unique())
    )

    Nitrogen = st.slider(
        "🌱 Nitrogen (ppm)",
        min_value=float(df["Nitrogen"].min()),
        max_value=float(df["Nitrogen"].max()),
        value=float(df["Nitrogen"].median()),
        format="%.1f"
    )

    Phosphorus = st.slider(
        "🌿 Phosphorus (ppm)",
        min_value=float(df["Phosphorus"].min()),
        max_value=float(df["Phosphorus"].max()),
        value=float(df["Phosphorus"].median()),
        format="%.1f"
    )

# =====================================
# COLUMN 2
# =====================================
with col2:

    Potassium = st.slider(
        "🌾 Potassium (ppm)",
        min_value=float(df["Potassium"].min()),
        max_value=float(df["Potassium"].max()),
        value=float(df["Potassium"].median()),
        format="%.1f"
    )

    Drought_Index = st.slider(
        "🔥 Drought Index",
        min_value=float(df["Drought_Index"].min()),
        max_value=float(df["Drought_Index"].max()),
        value=float(df["Drought_Index"].median()),
        format="%.2f"
    )

    Water_Stress_Index = st.slider(
        "💧 Water Stress Index",
        min_value=float(df["Water_Stress_Index"].min()),
        max_value=float(df["Water_Stress_Index"].max()),
        value=float(df["Water_Stress_Index"].median()),
        format="%.2f"
    )

# =====================================
# COLUMN 3
# =====================================
with col3:

    Fertilizer_Usage = st.selectbox(
        "🪴 Fertilizer Usage",
        sorted(df["Fertilizer_Usage"].dropna().unique())
    )

    Rainfall_mm = st.number_input(
        "🌧️ Rainfall (mm)",
        min_value=float(df["Rainfall_mm"].min()),
        max_value=float(df["Rainfall_mm"].max()),
        value=float(df["Rainfall_mm"].median()),
        format="%.1f"
    )

    Temperature_C = st.slider(
        "🌡️ Temperature (°C)",
        min_value=float(df["Temperature_C"].min()),
        max_value=float(df["Temperature_C"].max()),
        value=float(df["Temperature_C"].median()),
        format="%.1f"
    )
# ======================
# PREDICT BUTTON
# ======================
if st.button("🔍 Predict Tree Growth Rate", use_container_width=True,type="primary"):

    # ----------------------
    # CREATE INPUT DATAFRAME
    # ----------------------
    input_dict = {
    "Tree_Name": tree_name,
    "Nitrogen_ppm": Nitrogen,
    "potassium_ppm": Potassium,
    "Phosphorus_ppm": Phosphorus,
    "Drought_Index": Drought_Index,
    "Water_Stress_Index": Water_Stress_Index,
    "fertilizer_Usage": Fertilizer_Usage,
    "Rainfall_mm": Rainfall_mm,
    "Temperature_C": Temperature_C
}

    base_df = pd.DataFrame([input_dict])

    # ----------------------
    # ENCODE CATEGORICAL COLUMNS
    # ----------------------
    # 1) Frequency maps (e.g. Tree_Name, City, State_Province)
    if isinstance(freq_maps, dict):
        for col, mapping in freq_maps.items():
            if col in base_df.columns:
                base_df[col] = base_df[col].map(mapping).fillna(0.0)

    # 2) Ordinal mappings from saved ordinal encoder
    for feature in ordinal_feature_names:
        if feature in base_df.columns and feature in ordinal_maps:
            base_df[feature] = base_df[feature].map(ordinal_maps[feature]).fillna(0.0)

    # 3) Binary mappings for Yes/No fields
    binary_map = {"Yes": 1.0, "No": 0.0}
    for col in ["Pest_Presence", "Fungal_Infection"]:
        if col in base_df.columns:
            base_df[col] = base_df[col].map(binary_map).fillna(0.0)

# Match training columns for growth rate predication
    
    growth_input = base_df.copy()

    growth_input = growth_input.reindex(
    columns=growth_features,
    fill_value=0
)

    # growth_rate predication
    
    growth_rate = growth_model.predict(growth_input)[0]
  
   
# =====================================
# GROWTH STATUS
# =====================================

    # Dataset Thresholds
    LOW_THRESHOLD = 0.288
    HIGH_THRESHOLD = 0.497
    MAX_GROWTH = 0.650

    # Growth Category
    if growth_rate >= HIGH_THRESHOLD:
        growth_status = "🟢 High Growth"
        growth_color = "#2E7D32"

    elif growth_rate >= LOW_THRESHOLD:
        growth_status = "🟡 Moderate Growth"
        growth_color = "#FB8C00"

    else:
        growth_status = "🔴 Low Growth"
        growth_color = "#D32F2F"

    # Growth Score (0-100)
    growth_score = min(
        100,
        max(
            0,
            (float(growth_rate) / MAX_GROWTH) * 100
        )
    )

    # =====================================
    # MAIN LAYOUT
    # =====================================

    chart_col1, chart_col2 = st.columns([1, 1])

    # =====================================
    # LEFT SIDE
    # =====================================

    with chart_col1:

        with st.container(border=True):

            st.subheader("🌱 Growth Performance Analysis")

            gauge = go.Figure(
                go.Indicator(
                    mode="gauge+number",

                    value=float(growth_rate),

                    number={
                        "suffix": " m/yr",
                        "font": {
                            "size": 42,
                            "color": "#1B5E20"
                        }
                    },

                    title={
                        "text": "<b>Growth Rate</b>",
                        "font": {"size": 22}
                    },

                    gauge={

                        "axis": {
                            "range": [0, MAX_GROWTH],
                            "tickwidth": 2
                        },

                        "bar": {
                            "color": growth_color,
                            "thickness": 0.30
                        },

                        "steps": [

                            {
                                "range": [0, LOW_THRESHOLD],
                                "color": "#FFEBEE"
                            },

                            {
                                "range": [LOW_THRESHOLD, HIGH_THRESHOLD],
                                "color": "#FFF3E0"
                            },

                            {
                                "range": [HIGH_THRESHOLD, MAX_GROWTH],
                                "color": "#E8F5E9"
                            }
                        ],

                        "threshold": {
                            "line": {
                                "color": "#1B5E20",
                                "width": 5
                            },
                            "value": HIGH_THRESHOLD
                        }
                    }
                )
            )

            gauge.update_layout(
                height=350,
                margin=dict(l=20, r=20, t=40, b=20),
                paper_bgcolor="rgba(0,0,0,0)"
            )

            st.plotly_chart(
                gauge,
                use_container_width=True,
                config={"displayModeBar": False}
            )

            # Status Badge
            st.markdown(
                f"""
                <div style="
                    background:{growth_color};
                    padding:12px;
                    border-radius:10px;
                    text-align:center;
                    color:white;
                    font-size:18px;
                    font-weight:bold;
                    margin-top:10px;
                ">
                    {growth_status}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("##### 📈 Growth Score")

            st.progress(int(growth_score))

            st.metric(
                label="Overall Growth Score",
                value=f"{growth_score:.0f}/100"
            )

    # =====================================
    # RIGHT SIDE
    # =====================================

    with chart_col2:

        with st.container(border=True):

            st.subheader("📊 Growth KPIs")

            k1, k2, k3 = st.columns(3)

            with k1:
                st.metric(
                    "Current Rate",
                    f"{growth_rate:.3f}"
                )

            with k2:
                st.metric(
                    "Benchmark",
                    f"{HIGH_THRESHOLD:.3f}"
                )

            with k3:
                st.metric(
                    "Status",
                    growth_status.replace("🟢", "")
                                .replace("🟡", "")
                                .replace("🔴", "")
                )

        with st.container(border=True):

            st.subheader("🎯 Growth Benchmark")

            benchmark_df = pd.DataFrame({
                "Category": [
                    "Low",
                    "Moderate",
                    "High"
                ],
                "Growth": [
                    LOW_THRESHOLD,
                    (LOW_THRESHOLD + HIGH_THRESHOLD) / 2,
                    HIGH_THRESHOLD
                ]
            })

            benchmark_fig = px.bar(
                benchmark_df,
                x="Category",
                y="Growth",
                text="Growth"
            )

            benchmark_fig.add_hline(
                y=float(growth_rate),
                line_dash="dash",
                annotation_text=f"Current: {growth_rate:.3f}"
            )

            benchmark_fig.update_layout(
                height=280,
                showlegend=False,
                margin=dict(l=20, r=20, t=20, b=20)
            )

            st.plotly_chart(
                benchmark_fig,
                use_container_width=True
            )

    # =====================================
    # INTERPRETATION PANEL
    # =====================================

    with st.expander("📖 Growth Interpretation", expanded=False):

        st.markdown(f"""
    ### 🌳 Growth Summary

    **Current Growth Rate:** `{growth_rate:.3f} m/year`

    | Growth Rate | Category |
    |------------|-----------|
    | < 0.288 | 🔴 Low Growth |
    | 0.288 - 0.497 | 🟡 Moderate Growth |
    | ≥ 0.497 | 🟢 High Growth |

    ### Recommendation

    - Maintain adequate irrigation.
    - Monitor nitrogen, phosphorus and potassium levels.
    - Reduce drought and water stress conditions.
    - Apply fertilizer when needed.
    - Improve soil fertility for sustainable growth.

    """)

st.markdown("""
---
<div style='text-align:center; color:green;'>
<h4>🌳 Tree Growth Prediction System</h4>
<p>Predicting Future Tree Growth Through Machine Learning and Environmental Intelligence</p>
</div>
""", unsafe_allow_html=True)        