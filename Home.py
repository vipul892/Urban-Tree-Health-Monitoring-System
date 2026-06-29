import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
import pydeck as pdk

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Urban Tree Health Monitering Dashboard",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# LOAD DATA
# =====================================

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


/* Sidebar Header */
.sidebar-header{
    text-align:center;
    margin-top:10px;
    margin-bottom:10px;
}

.sidebar-header h2{
    color:white;
    font-size:22px;
    font-weight:700;
    margin-bottom:0px;
}

.sidebar-header p{
    color:#d8f3dc;
    font-size:13px;
    margin-top:2px;
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
            
/* KPI Card */
[data-testid="metric-container"]{
    background: white;
    padding: 18px;
    border-radius: 15px;
    border-left: 5px solid #28a745;

    box-shadow: 0px 2px 8px rgba(0,0,0,0.10);

    transition: all 0.3s ease-in-out;

    cursor: pointer;
}

/* Hover Effect */
[data-testid="metric-container"]:hover{

    transform: translateY(-10px) scale(1.05);

    box-shadow:
        0px 15px 30px rgba(0,0,0,0.20);

    border-left: 5px solid #145A32;
}

/* KPI Value */
[data-testid="stMetricValue"]{
    color:#145A32;
    font-size:28px;
    font-weight:bold;
}

/* KPI Label */
[data-testid="metric-container"] label{
    color:#666;
    font-weight:600;
}

/* Selectbox */
div[data-baseweb="select"]{
    border-radius:10px;
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

  

# # =====================================
# # HEADER
# # =====================================

# h1, h2, h3 = st.columns([10,2,2],gap="small")

# with h1:

#     st.title("🌳 Urban Tree Health Monitoring")

#     st.markdown("""
#                 Smart Monitoring for Sustainable Urban Forests
#                 """)


# with h2:

#     state = st.selectbox(
#         "🔍 Search State",
#         ["All"] + sorted(df["State_Province"].dropna().unique())
#     )

# with h3:

#     city = st.selectbox(
#         "🏙 Search City",
#         ["All"] + sorted(df["City"].dropna().unique())
#     )

# st.divider()

# # =====================================
# # FILTER DATA
# # =====================================

# filtered_df = df.copy()

# if state != "All":
#     filtered_df = filtered_df[
#         filtered_df["State_Province"] == state
#     ]

# if city != "All":
#     filtered_df = filtered_df[
#         filtered_df["City"] == city
#     ]


# # =====================================
# # KPI CARDS
# # =====================================

# total_trees = len(filtered_df)

# healthy = len(
#     filtered_df[
#         filtered_df["Tree_Health_Status"] == "Excellent"
#     ]
# )

# at_risk = len(
#     filtered_df[
#         filtered_df["Tree_Health_Status"] == "Poor"
#     ]
# )

# avg_aqi = round(
#     filtered_df["AQI"].mean(),
#     0
# )

# avg_carbon = round(
#     filtered_df["Carbon_Absorption_kg"].mean(),
#     2
# )

# survival = round(
#     filtered_df["Survival_Probability"].mean() * 100,
#     1
# )

# col1,col2,col3,col4,col5,col6 = st.columns(6,gap="small")

# with col1:
#     st.metric(
#         "🌳 Total Trees",
#         f"{total_trees:,}"
#     )

# with col2:
#     st.metric(
#         "💚 Healthy Trees",
#         f"{healthy:,}"
#     )

# with col3:
#     st.metric(
#         "⚠️ At Risk Trees",
#         f"{at_risk:,}"
#     )

# with col4:
#     st.metric(
#         "🌫 AQI",
#         f"{avg_aqi:.0f}"
#     )

# with col5:
#     st.metric(
#         "🌱 Avg Carbon",
#         f"{avg_carbon:.2f} kg"
#     )

# with col6:
#     st.metric(
#         "📈 Survival",
#         f"{survival:.1f}%"
#     )
# st.divider()

# st.markdown("<br>", unsafe_allow_html=True)

# col1,col2,col3,col4,col5,col6 = st.columns(6, gap="small")


# # =====================================
# # ROW 1 - HEALTH DISTRIBUTION
# # =====================================

# c1, c2 = st.columns(2)

# with c1:

#     st.markdown("### 🌳 Tree Health Distribution")

#     health_df = (
#         filtered_df["Tree_Health_Status"]
#         .value_counts()
#         .reset_index()
#     )

#     health_df.columns = ["Health Status", "Count"]

#     fig = px.pie(
#         health_df,
#         names="Health Status",
#         values="Count",
#         hole=0.65,
#         color="Health Status",
#         color_discrete_map={
#             "Healthy": "#2E8B57",
#             "Moderate": "#F4B400",
#             "Poor": "#DB4437"
#         }
#     )

#     # Labels inside chart
#     fig.update_traces(
#         textposition="inside",
#         textinfo="percent+label",
#         hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}"
#     )

#     # Donut center text
#     total_trees = health_df["Count"].sum()

#     fig.add_annotation(
#         text=f"<b>{total_trees}</b><br>Trees",
#         x=0.5,
#         y=0.5,
#         showarrow=False,
#         font=dict(size=18)
#     )

#     fig.update_layout(
#         height=350,
#         margin=dict(t=20, b=20, l=20, r=20),
#         legend=dict(
#             orientation="h",
#             y=-0.15,
#             x=0.5,
#             xanchor="center"
#         ),
#         paper_bgcolor="rgba(0,0,0,0)",
#         plot_bgcolor="rgba(0,0,0,0)"
#     )

#     st.plotly_chart(
#         fig,
#         use_container_width=True
#     )

# with c2:

#     st.markdown("### 📍 Top 5 States by Tree Records")

#     state_df = (
#         filtered_df.groupby("State_Province")
#         .size()
#         .reset_index(name="Trees")
#         .sort_values("Trees", ascending=False)
#         .head(5)
#     )

#     fig2 = px.bar(
#         state_df,
#         y="State_Province",
#         x="Trees",
#         orientation="h",
#         text="Trees"
#     )

#     fig2.update_traces(
#         marker=dict(
#             color="#2E8B57",      # Forest Green
#             line=dict(
#                 color="#145A32",  # Dark Green Border
#                 width=1
#             )
#         ),
#         textposition="outside",
#         hovertemplate="<b>%{y}</b><br>Tree Count: %{x}<extra></extra>"
#     )

#     fig2.update_layout(
#         height=350,
#         margin=dict(t=20, b=20, l=20, r=20),
#         xaxis_title="Number of Trees",
#         yaxis_title="",
#         showlegend=False,
#         plot_bgcolor="rgba(0,0,0,0)",
#         paper_bgcolor="rgba(0,0,0,0)",
#         font=dict(size=12),
#         xaxis=dict(
#             showgrid=True,
#             gridcolor="rgba(200,200,200,0.2)",
#             zeroline=False
#         ),
#         yaxis=dict(
#             showgrid=False,
#             categoryorder="total ascending"
#         )
#     )

#     st.plotly_chart(
#         fig2,
#         use_container_width=True,
#         config={"displayModeBar": False}
#     )


# # =====================================
# # HEALTH ANALYSIS
# # =====================================

# g1, g2 = st.columns(2)

# with g1:

#     st.markdown("### 🌿 Top 10 Carbon Absorbing Trees")

#     carbon_df = (
#         filtered_df.groupby("Tree_Name")["Carbon_Absorption_kg"]
#         .mean()
#         .sort_values(ascending=False)
#         .head(10)
#         .reset_index()
#     )

#     fig3 = px.bar(
#         carbon_df,
#         y="Tree_Name",
#         x="Carbon_Absorption_kg",
#         orientation="h",
#         text=carbon_df["Carbon_Absorption_kg"].round(1)
#     )

#     fig3.update_traces(
#         marker=dict(
#             color="#228B22",      # Forest Green
#             line=dict(
#                 color="#145A32",
#                 width=1
#             )
#         ),
#         textposition="outside",
#         hovertemplate=
#         "<b>%{y}</b><br>" +
#         "Carbon Absorption: %{x:.2f} kg<extra></extra>"
#     )

#     fig3.update_layout(
#         height=350,
#         margin=dict(l=10, r=10, t=20, b=10),
#         xaxis_title="Average Carbon Absorption (kg)",
#         yaxis_title="",
#         showlegend=False,
#         plot_bgcolor="rgba(0,0,0,0)",
#         paper_bgcolor="rgba(0,0,0,0)",
#         xaxis=dict(
#             showgrid=True,
#             gridcolor="rgba(200,200,200,0.2)"
#         ),
#         yaxis=dict(
#             showgrid=False,
#             categoryorder="total ascending"
#         )
#     )

#     st.plotly_chart(
#         fig3,
#         use_container_width=True,
#         config={"displayModeBar": False}
#     )

# with g2:

#     st.markdown("### 💧 Water Stress Distribution")

#     stress_df = (
#         filtered_df["Water_Stress_Index"]
#         .value_counts()
#         .reset_index()
#     )

#     stress_df.columns = ["Stress", "Count"]

#     color_map = {
#         "Low": "#2E8B57",      # Green
#         "Medium": "#F4B400",  # Yellow
#         "High": "#DB4437"     # Red
#     }

#     fig4 = px.bar(
#         stress_df,
#         x="Stress",
#         y="Count",
#         text="Count",
#         color="Stress",
#         color_discrete_map=color_map
#     )

#     fig4.update_traces(
#         textposition="outside",
#         hovertemplate="<b>%{x}</b><br>Count: %{y}<extra></extra>"
#     )

#     fig4.update_layout(
#         height=350,
#         margin=dict(l=10, r=10, t=20, b=10),
#         xaxis_title="Water Stress Level",
#         yaxis_title="Number of Trees",
#         showlegend=False,
#         plot_bgcolor="rgba(0,0,0,0)",
#         paper_bgcolor="rgba(0,0,0,0)",
#         xaxis=dict(showgrid=False),
#         yaxis=dict(
#             showgrid=True,
#             gridcolor="rgba(200,200,200,0.2)"
#         )
#     )

#     st.plotly_chart(
#         fig4,
#         use_container_width=True,
#         config={"displayModeBar": False}
#     )

# st.divider()

# col1, col2 = st.columns([3, 1], gap="small")

# # =====================================
# # MAP VISUALIZATION
# # =====================================

# import pydeck as pdk
# import pandas as pd

# with col1:

#     st.markdown("### 🌍 Urban Tree Earth View (2D)")

#     # =========================
#     # CLEAN DATA
#     # =========================
#     map_df = filtered_df.copy()
#     map_df = map_df.dropna(subset=["Latitude", "Longitude"])

#     map_df["Latitude"] = pd.to_numeric(map_df["Latitude"], errors="coerce")
#     map_df["Longitude"] = pd.to_numeric(map_df["Longitude"], errors="coerce")
#     map_df = map_df.dropna(subset=["Latitude", "Longitude"])

#     map_df = map_df.head(1500)

#     # =========================
#     # COLOR ENGINE
#     # =========================
#     def get_color(status):
#         if status == "Healthy":
#             return [0, 255, 157]
#         elif status == "At Risk":
#             return [255, 176, 32]
#         else:
#             return [255, 77, 77]

#     map_df["color"] = map_df["Tree_Health_Status"].apply(get_color)

#     # =========================
#     # FIXED MARKER SIZE (IMPORTANT)
#     # =========================
#     layer = pdk.Layer(
#         "ScatterplotLayer",
#         data=map_df,
#         get_position='[Longitude, Latitude]',

#         get_color="color",

#         # 🔥 FIX: proper visible size
#         get_radius=2500,   # (8000 was unstable; 2000–3000 is ideal)

#         radius_min_pixels=4,   # ensures visibility even when zoomed out
#         radius_max_pixels=25,  # prevents oversize at zoom in

#         opacity=0.9,
#         pickable=True,
#         auto_highlight=True
#     )

#     # =========================
#     # FIXED VIEW (MAP ZOOM BIGGER FEEL)
#     # =========================
#     view_state = pdk.ViewState(
#         latitude=map_df["Latitude"].mean(),
#         longitude=map_df["Longitude"].mean(),

#         zoom=5,        # good city-level view
#         pitch=0,       # 2D
#         bearing=0
#     )

#     # =========================
#     # MAP
#     # =========================
#     deck = pdk.Deck(
#         layers=[layer],
#         initial_view_state=view_state,
#         map_style="https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json",
#         tooltip={
#             "html": """
#                 <b>🌳 Tree:</b> {Tree_Name}<br/>
#                 <b>🌿 Health:</b> {Tree_Health_Status}<br/>
#                 <b>🌫 AQI:</b> {AQI}<br/>
#                 <b>📍 City:</b> {City}<br/>
#                 <b>🌎 State:</b> {State_Province}
#             """,
#             "style": {
#                 "backgroundColor": "black",
#                 "color": "white"
#             }
#         }
#     )

#     st.pydeck_chart(deck, use_container_width=True)
# # =====================================
# # ENVIRONMENTAL METRICS
# # =====================================

# with col2:

#     st.markdown("### 🌍 Environmental Overview")

#     st.markdown("""
#     <style>
#     .env-card {
#     background-color: #f8f9fa;
#     padding: 8px 12px;
#     border-radius: 6px;
#     margin-bottom: 6px;
#     border-left: 3px solid #2E8B57;
#     }

#     .env-icon {
#     font-size: 22px;
#     }

#     .env-title {
#     font-size: 17px;
#     color: black;
    
#     }

#     .env-value {
#     font-size: 18px;
#     font-weight: bold;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="env-card">
#         <div class="env-icon">🌫️</div>
#         <div class="env-title">Average AQI</div>
#         <div class="env-value">{filtered_df['AQI'].mean():.0f}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="env-card">
#         <div class="env-icon">🌡️</div>
#         <div class="env-title">Temperature</div>
#         <div class="env-value">{filtered_df['Temperature_C'].mean():.1f} °C</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="env-card">
#         <div class="env-icon">💧</div>
#         <div class="env-title">Humidity</div>
#         <div class="env-value">{filtered_df['Humidity_Pct'].mean():.1f}%</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="env-card">
#         <div class="env-icon">🌧️</div>
#         <div class="env-title">Rainfall</div>
#         <div class="env-value">{filtered_df['Rainfall_mm'].mean():.1f} mm</div>
#     </div>
#     """, unsafe_allow_html=True)

# # =====================================
# # TREES REQUIRING ATTENTION
# # =====================================

# st.markdown("### 🚨 Trees Requiring Attention")

# attention_df = filtered_df[
#     filtered_df["Tree_Health_Status"] != "Healthy"
# ][
#     [
#         "Tree_Name",
#         "State_Province",
#         "City",
#         "Tree_Health_Status",
#         "AQI",
#         "Water_Stress_Index",
#         "Disease_Symptoms",
#         "Fungal_Infection",
#         "Survival_Probability"
#     ]
# ].head(100)

# # Clean table display (NO analysis styling)
# st.dataframe(
#     attention_df,
#     use_container_width=True,
#     height=450
# )

#     # -----------------------------
#     # FOOTER
#     # -----------------------------

# st.markdown("""
# ---
# <div style='text-align:center; color:green;'>
# <h4>🌳 Urban Tree Health Monitoring System | Smart Monitoring for Sustainable Urban Forests</h4>
# <p>Powered by Machine Learning • Environmental Analytics • Sustainable Urban Forestry</p>
# </div>
# """, unsafe_allow_html=True)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🌳 Urban Tree Health Monitoring & Plantation Recommendation System")
st.caption("🌿 AI-Powered Smart Urban Forestry")

st.divider()

# --------------------------------------------------
# INTRODUCTION
# --------------------------------------------------
st.markdown("""
Welcome to the **Urban Tree Health Monitoring & Plantation Recommendation System**.

This intelligent platform uses **Machine Learning** to monitor tree health,
predict growth and survival, estimate carbon absorption, and recommend the
most suitable tree species for plantation.

It supports **sustainable urban planning** and helps build **greener,
healthier, and smarter cities**.
""")

st.divider()

# --------------------------------------------------
# FEATURES
# --------------------------------------------------
st.subheader("🚀 Features")

col1, col2 = st.columns(2)

with col1:
    st.info("""
### 🌳 Tree Health Prediction
Predict whether a tree is **Excellent, Good, or Poor**.
""")

    st.success("""
### 📈 Growth Rate Prediction
Estimate future tree growth using environmental data.
""")

    st.warning("""
### 🌍 Carbon Estimation
Predict the tree's carbon absorption potential.
""")

with col2:
    st.info("""
### 🌱 Survival Probability
Estimate the likelihood of successful tree survival.
""")

    st.success("""
### 🌿 Plantation Recommendation
Recommend the most suitable tree species based on
soil and climate conditions.
""")

st.divider()

# --------------------------------------------------
# MACHINE LEARNING MODELS
# --------------------------------------------------
st.subheader("🤖 Machine Learning Models")

col1, col2 = st.columns(2)

with col1:
    st.metric("🌳 Health Prediction", "CatBoost Classifier")
    st.metric("📈 Growth Prediction", "XGBoost Regressor")

with col2:
    st.metric("🌍 Carbon Estimation", "XGBoost Regressor")
    st.metric("🌱 Survival Prediction", "CatBoost Regressor")

st.divider()

# --------------------------------------------------
# MISSION
# --------------------------------------------------
st.subheader("🌱 Mission")

st.markdown(
    """
> **Empowering smarter cities with AI-driven tree monitoring and sustainable plantation recommendations.**
"""
)

st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    """
<div style="text-align:center; font-size:22px; font-weight:bold; color:#2E8B57;">
💚 Grow Green • Predict Smart • Build Sustainable Cities 🌳
</div>
""",
unsafe_allow_html=True,
)