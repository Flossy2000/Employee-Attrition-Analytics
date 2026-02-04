
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(page_title="Employee Attrition Dashboard", layout="wide")

# ---------------------------
# Load data
# ---------------------------
df = pd.read_csv("IBM HR Employee Attrition Data.csv")

# ---------------------------
# Title
# ---------------------------
st.title("Employee Attrition Dashboard")
st.write("Interactive dashboard to explore key drivers of employee attrition")

# ---------------------------
# Sidebar filters
# ---------------------------
st.sidebar.header("Filters")

department = st.sidebar.selectbox(
    "Select Department",
    ["All"] + list(df["Department"].unique())
)

job_level = st.sidebar.selectbox(
    "Select Job Level",
    ["All"] + sorted(df["JobLevel"].unique().tolist())
)

if department != "All":
    df = df[df["Department"] == department]

if job_level != "All":
    df = df[df["JobLevel"] == job_level]

# ---------------------------
# KPI Metrics
# ---------------------------
total_employees = df.shape[0]
attrition_count = df[df["Attrition"] == "Yes"].shape[0]
attrition_rate = round((attrition_count / total_employees) * 100, 2)

st.markdown("### Key Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", total_employees)
col2.metric("Employees Left", attrition_count)
col3.metric("Attrition Rate (%)", attrition_rate)

st.markdown("---")

# ---------------------------
# Visuals Row 1
# ---------------------------
col1, col2 = st.columns(2)

# ---- Visual 1: Overall Attrition ----
with col1:
    st.subheader("Overall Employee Attrition")
    fig1, ax1 = plt.subplots()
    df["Attrition"].value_counts().plot(kind="bar", ax=ax1)
    ax1.set_xlabel("Attrition")
    ax1.set_ylabel("Number of Employees")
    st.pyplot(fig1)

# ---- Visual 2: Attrition by Department ----
with col2:
    st.subheader("Attrition by Department")
    dept_attrition = df.groupby(["Department", "Attrition"]).size().unstack()
    fig2, ax2 = plt.subplots()
    dept_attrition["Yes"].plot(kind="bar", ax=ax2)
    ax2.set_xlabel("Department")
    ax2.set_ylabel("Employees Left")
    st.pyplot(fig2)

# ---------------------------
# Visuals Row 2
# ---------------------------
col3, col4 = st.columns(2)

# ---- Visual 3: Attrition by Overtime ----
with col3:
    st.subheader("Attrition by Overtime")
    overtime_attrition = df.groupby(["OverTime", "Attrition"]).size().unstack()
    fig3, ax3 = plt.subplots()
    overtime_attrition["Yes"].plot(kind="bar", ax=ax3)
    ax3.set_xlabel("Overtime")
    ax3.set_ylabel("Employees Left")
    st.pyplot(fig3)

# ---- Visual 4: Work-Life Balance vs Attrition ----
with col4:
    st.subheader("Attrition by Work-Life Balance")
    wlb_attrition = df.groupby(["WorkLifeBalance", "Attrition"]).size().unstack()
    fig4, ax4 = plt.subplots()
    wlb_attrition["Yes"].plot(kind="bar", ax=ax4)
    ax4.set_xlabel("Work-Life Balance Rating")
    ax4.set_ylabel("Employees Left")
    st.pyplot(fig4)

# ---------------------------
# Visual 5 (Full Width)
# ---------------------------
st.markdown("---")
st.subheader("Monthly Income Distribution by Attrition")

fig5, ax5 = plt.subplots()
df.boxplot(column="MonthlyIncome", by="Attrition", ax=ax5)
plt.suptitle("")
ax5.set_xlabel("Attrition")
ax5.set_ylabel("Monthly Income")
st.pyplot(fig5)


