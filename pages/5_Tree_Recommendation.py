import streamlit as st
import pandas as pd

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Tree Recommendation System",
    page_icon="🌳",
    layout="wide"
)

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

[data-testid="stMetric"]{
    background-color:#f8f9fa;
    padding:15px;
    border-radius:12px;
    border-left:5px solid #2E7D32;
}

div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] {
    gap: 0.5rem;
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
  


# ======================================================
# LOAD DATA
# ======================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/raw_data/trees_indian_dataset.csv")

df = load_data()

# ======================================================
# CREATE RULES
# ======================================================

@st.cache_data
def create_tree_rules(df):

    rules = {}

    for tree in df["Tree_Name"].dropna().unique():

        tree_df = df[df["Tree_Name"] == tree]

        if len(tree_df) < 3:
            continue

        soil_mode = tree_df["Soil_Type"].mode()

        rules[tree] = {

            "temp_min": tree_df["Temperature_C"].quantile(0.05),
            "temp_max": tree_df["Temperature_C"].quantile(0.95),

            "rain_min": tree_df["Rainfall_mm"].quantile(0.05),
            "rain_max": tree_df["Rainfall_mm"].quantile(0.95),

            "humidity_min": tree_df["Humidity_Pct"].quantile(0.05),
            "humidity_max": tree_df["Humidity_Pct"].quantile(0.95),

            "aqi_max": tree_df["AQI"].quantile(0.95),
            "pm25_max": tree_df["PM2_5"].quantile(0.95),
            "pm10_max": tree_df["PM10"].quantile(0.95),

            "drought_max": tree_df["Drought_Index"].quantile(0.95),

            "soil_type": soil_mode.iloc[0] if not soil_mode.empty else "Unknown",

            "ph_min": tree_df["Soil_pH"].quantile(0.05),
            "ph_max": tree_df["Soil_pH"].quantile(0.95),

            "elev_min": tree_df["Elevation"].quantile(0.05),
            "elev_max": tree_df["Elevation"].quantile(0.95)
        }

    return rules


# ======================================================
# RECOMMENDATION ENGINE
# ======================================================

def recommend_trees(
    tree_rules,
    temperature,
    rainfall,
    humidity,
    aqi,
    pm25,
    pm10,
    drought_index,
    soil_type,
    soil_ph,
    elevation,
    top_n=5
):

    recommendations = []

    MAX_SCORE = 110

    for tree, rule in tree_rules.items():

        score = 0

        if rule["temp_min"] <= temperature <= rule["temp_max"]:
            score += 20

        if rule["rain_min"] <= rainfall <= rule["rain_max"]:
            score += 20

        if rule["humidity_min"] <= humidity <= rule["humidity_max"]:
            score += 20

        if str(soil_type).lower() == str(rule["soil_type"]).lower():
            score += 15

        if rule["ph_min"] <= soil_ph <= rule["ph_max"]:
            score += 10

        if aqi <= rule["aqi_max"]:
            score += 4

        if pm25 <= rule["pm25_max"]:
            score += 3

        if pm10 <= rule["pm10_max"]:
            score += 3

        if drought_index <= rule["drought_max"]:
            score += 5

        if rule["elev_min"] <= elevation <= rule["elev_max"]:
            score += 10

        suitability = round((score / MAX_SCORE) * 100, 1)

        recommendations.append({
            "Tree_Name": tree,
            "Suitability (%)": suitability
        })

    result = pd.DataFrame(recommendations)

    return result.sort_values(
        "Suitability (%)",
        ascending=False
    ).head(top_n)


# ======================================================
# HEADER
# ======================================================

st.title("🌳 Tree Plantation Recommendation System")

st.markdown(
    "Select environmental conditions and get the best tree recommendations."
)

st.divider()

# ======================================================
# INPUT SECTION
# ======================================================

col1, col2, col3 = st.columns(3)

with col1:

    temperature = st.slider(
        "🌡 Temperature (°C)",
        min_value=float(df["Temperature_C"].min()),
        max_value=float(df["Temperature_C"].max()),
        value=float(df["Temperature_C"].median())
    )

    rainfall = st.slider(
        "🌧 Rainfall (mm)",
        min_value=float(df["Rainfall_mm"].min()),
        max_value=float(df["Rainfall_mm"].max()),
        value=float(df["Rainfall_mm"].median())
    )

    humidity = st.slider(
        "💧 Humidity (%)",
        min_value=float(df["Humidity_Pct"].min()),
        max_value=float(df["Humidity_Pct"].max()),
        value=float(df["Humidity_Pct"].median())
    )

with col2:

    aqi = st.slider(
        "🏭 AQI",
        min_value=float(df["AQI"].min()),
        max_value=float(df["AQI"].max()),
        value=float(df["AQI"].median())
    )

    pm25 = st.slider(
        "🌫 PM2.5",
        min_value=float(df["PM2_5"].min()),
        max_value=float(df["PM2_5"].max()),
        value=float(df["PM2_5"].median())
    )

    pm10 = st.slider(
        "🌫 PM10",
        min_value=float(df["PM10"].min()),
        max_value=float(df["PM10"].max()),
        value=float(df["PM10"].median())
    )

with col3:

    drought_index = st.slider(
        "☀ Drought Index",
        min_value=float(df["Drought_Index"].min()),
        max_value=float(df["Drought_Index"].max()),
        value=float(df["Drought_Index"].median())
    )

    soil_type = st.selectbox(
        "🌱 Soil Type",
        sorted(df["Soil_Type"].dropna().unique())
    )

    soil_ph = st.slider(
        "🧪 Soil pH",
        min_value=float(df["Soil_pH"].min()),
        max_value=float(df["Soil_pH"].max()),
        value=float(df["Soil_pH"].median())
    )

    elevation = st.slider(
        "⛰ Elevation",
        min_value=float(df["Elevation"].min()),
        max_value=float(df["Elevation"].max()),
        value=float(df["Elevation"].median())
    )

# ======================================================
# RECOMMEND BUTTON
# ======================================================

tree_rules = create_tree_rules(df)

if st.button("🌱 Recommend Trees", use_container_width=True,type="primary"):

    recommendations = recommend_trees(
        tree_rules,
        temperature,
        rainfall,
        humidity,
        aqi,
        pm25,
        pm10,
        drought_index,
        soil_type,
        soil_ph,
        elevation
    )

    st.divider()

    st.subheader("🏆 Top Recommended Trees")

    # ==========================================
    # SUMMARY METRICS
    # ==========================================

    top_tree = recommendations.iloc[0]["Tree_Name"]
    top_score = recommendations.iloc[0]["Suitability (%)"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🌳 Trees Evaluated",
            len(tree_rules)
        )

    with col2:
        st.metric(
            "🥇 Best Match",
            top_tree
        )

    with col3:
        st.metric(
            "🎯 Top Suitability",
            f"{top_score:.1f}%"
        )

    st.markdown("---")

    # ==========================================
    # TREE RECOMMENDATION CARDS
    # ==========================================

    medals = {
        1: "🥇",
        2: "🥈",
        3: "🥉"
    }

    for rank, row in enumerate(
        recommendations.itertuples(index=False),
        start=1
    ):

        tree_name = row[0]
        score = row[1]

        if score >= 90:
            status = "🌟 Excellent Match"

        elif score >= 75:
            status = "✅ Very Good Match"

        elif score >= 60:
            status = "👍 Good Match"

        else:
            status = "⚠️ Moderate Match"

        medal = medals.get(rank, "🌳")

        with st.container(border=True):

            col1, col2 = st.columns([4, 1])

            with col1:

                st.markdown(
                    f"### {medal} {tree_name}"
                )

                st.progress(score / 100)

                st.caption(status)

            with col2:

                st.metric(
                    "Score",
                    f"{score:.1f}%"
                )

                st.write(f"Rank #{rank}")

    st.markdown("---")

    # ==========================================
    # DOWNLOAD BUTTON
    # ==========================================

    csv = recommendations.to_csv(index=False)

    st.download_button(
        label="📥 Download Recommendations",
        data=csv,
        file_name="tree_recommendations.csv",
        mime="text/csv",
        use_container_width=True
    )

st.markdown("""
---
<div style='text-align:center; color:green;'>
<h4>🌱 Tree Plantation Recommendation System</h4>
<p>Recommending the Right Trees for Sustainable and Greener Urban Environments</p>
</div>
""", unsafe_allow_html=True)