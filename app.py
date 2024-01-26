import streamlit as st
import pandas as pd
import plotly.express as px

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")
data["DateTime"] = pd.to_datetime(data["DateTime"], format="%Y-%m-%d")

# Sidebar for filters
st.sidebar.header("Filter Options")
metal = st.sidebar.selectbox("Select Metal", data.columns[1:], index=0)

date_range = st.sidebar.date_input("Select Date Range", [data["DateTime"].min().date(), data["DateTime"].max().date()])

filtered_data = data.loc[(data["DateTime"] >= date_range[0]) & (data["DateTime"] <= date_range[1])]

# Plot the data
st.title("Precious Metal Prices 2018-2021")
st.header("Metal Prices Over Time")
fig = px.line(
    filtered_data,
    x="DateTime",
    y=[metal],
    title=f"{metal} Prices 2018-2021",
    labels={"DateTime": "Date", metal: "Price (USD/oz)"},
    line_shape="linear",
    template="plotly_dark",
    color_discrete_map={
        "Platinum": "#E5E4E2",
        "Gold": "gold",
        "Silver": "silver",
        "Palladium": "#CED0DD",
        "Rhodium": "#E2E7E1",
        "Iridium": "#3D3C3A",
        "Ruthenium": "#C9CBC8"
    }
)
st.plotly_chart(fig)
