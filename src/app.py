
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Used Car Market Analysis Dashboard")

# Load data
df = pd.read_csv('data/used_cars_mock.csv')

# Sidebar filters for interactivity
brand = st.sidebar.multiselect("Select Brands", options=df['brand'].unique())
price_range = st.sidebar.slider("Price Range", 0, 100000, (500, 50000))

# Filtered Chart
filtered_df = df[df['brand'].isin(brand)]
fig = px.scatter(filtered_df, x='age', y='price', color='brand')
st.plotly_chart(fig)