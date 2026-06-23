import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

from sklearn.ensemble import RandomForestRegressor

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Research Data Impact Dashboard",
    layout="wide"
)

st.title("Making Complex Data Useful")
st.subheader(
    "Helping non-specialists understand the value of a research dataset"
)

# --------------------------------------------------
# SIMULATED DATA
# Replace with real data later
# --------------------------------------------------

np.random.seed(42)

n = 3000

df = pd.DataFrame({
    "age": np.random.randint(18,80,n),
    "financial_strain": np.random.normal(50,15,n),
    "social_support": np.random.normal(60,12,n),
    "sleep_quality": np.random.normal(65,10,n),
    "exercise": np.random.normal(55,15,n)
})

df["wellbeing"] = (
    100
    - 0.5*df["financial_strain"]
    + 0.4*df["social_support"]
    + 0.3*df["sleep_quality"]
    + np.random.normal(0,8,n)
)

# --------------------------------------------------
# TOP KPIs
# --------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

c1.metric("Participants", "25,000+")
c2.metric("Years of Data", "10")
c3.metric("Data Waves", "12")
c4.metric("Variables", "1,000+")

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Explore")

selected_outcome = st.sidebar.selectbox(
    "Outcome",
    ["wellbeing"]
)

age_min, age_max = st.sidebar.slider(
    "Age Range",
    18,80,(18,80)
)

filtered = df[
    (df.age >= age_min) &
    (df.age <= age_max)
]

# --------------------------------------------------
# ROW 1
# --------------------------------------------------

left,right = st.columns(2)

# ---------------------------------
# UNDERSTAND PEOPLE IN CONTEXT
# ---------------------------------

with left:

    st.subheader("1. Understand People in Context")

    fig = px.scatter(
        filtered,
        x="financial_strain",
        y="wellbeing",
        color="age",
        opacity=0.6,
        title="Financial strain vs wellbeing"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------
# CHANGE OVER TIME
# ---------------------------------

with right:

    st.subheader("2. Track Change Over Time")

    waves = np.arange(1,13)

    trend = pd.DataFrame({
        "wave": waves,
        "18-29": 70 + np.sin(waves/2)*5,
        "30-49": 75 + np.sin(waves/2+1)*4,
        "50-64": 80 + np.sin(waves/2+2)*3,
        "65+": 78 + np.sin(waves/2+3)*4
    })

    fig = go.Figure()

    for col in trend.columns[1:]:
        fig.add_trace(
            go.Scatter(
                x=trend["wave"],
                y=trend[col],
                mode="lines+markers",
                name=col
            )
        )

    fig.update_layout(
        title="Wellbeing trajectories"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# ROW 2
# --------------------------------------------------

left,right = st.columns(2)

# ---------------------------------
# WHAT SHAPES OUTCOMES?
# ---------------------------------

with left:

    st.subheader("3. Explore What Shapes Outcomes")

    X = filtered[
        [
            "financial_strain",
            "social_support",
            "sleep_quality",
            "exercise"
        ]
    ]

    y = filtered["wellbeing"]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X,y)

    imp = pd.DataFrame({
        "factor": X.columns,
        "importance": model.feature_importances_
    })

    imp = imp.sort_values(
        "importance",
        ascending=True
    )

    fig = px.bar(
        imp,
        x="importance",
        y="factor",
        orientation="h",
        title="Relative importance of predictors"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------
# POLICY IMPACT
# ---------------------------------

with right:

    st.subheader("4. Inform Policy and Practice")

    region_df = pd.DataFrame({
        "Region": [
            "North",
            "Midlands",
            "South",
            "Scotland",
            "Wales"
        ],
        "Wellbeing": [
            68,72,77,75,71
        ]
    })

    fig = px.bar(
        region_df,
        x="Region",
        y="Wellbeing",
        title="Regional differences"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# RESEARCH QUESTIONS
# --------------------------------------------------

st.divider()

st.subheader("Questions This Dataset Can Answer")

questions = [
    "How do financial pressures affect mental health?",
    "What role does social connection play in wellbeing?",
    "Do life events create lasting psychological change?",
    "Which groups are most resilient?",
    "How does wellbeing evolve over time?"
]

for q in questions:
    st.markdown(f"✅ {q}")

# --------------------------------------------------
# IMPACT STORY
# --------------------------------------------------

st.divider()

st.subheader("Why This Matters")

st.info("""
Instead of showing variables and codebooks, this dashboard
shows stakeholders:

• Who is represented in the data

• What societal questions can be answered

• Which factors matter most

• How outcomes change through time

• How findings can inform policy and interventions
""")
