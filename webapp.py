import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("data.txt")

st.title("Average World Temperature")
st.subheader("Below is a line graph to visualize the data")
figure = px.line(x=df["date"], y=df["temperature"], labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)