import streamlit as st
import plotly.express as px
import pandas as pd
import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("SELECT date FROM data")
date = cursor.fetchall()
date = [item[0] for item in date]

cursor.execute("SELECT temperature from data")
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]


st.title("Average World Temperature")
st.subheader("Below is a line graph to visualize the data")
figure = px.line(x=date, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)