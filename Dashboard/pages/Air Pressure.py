import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load custom CSS
css_file_path = os.path.join(os.path.dirname(__file__), "..", "styles.css")
with open(css_file_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the data
data = pd.read_csv('./cleaned_data.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Filter for Air Pressure (PRES)
pres_data = data[['timestamp', 'PRES']]

# Page title
st.title("Air Pressure (PRES) Visualizations")

# Line Chart
st.markdown("<div class='card'><h3>Air Pressure Over Time</h3></div>", unsafe_allow_html=True)
st.line_chart(pres_data.set_index('timestamp')['PRES'])

# Bar Chart
st.markdown("<div class='card'><h3>Air Pressure Distribution</h3></div>", unsafe_allow_html=True)
st.bar_chart(pres_data.set_index('timestamp')['PRES'])

# Pie Chart
st.markdown("<div class='card'><h3>Air Pressure Proportions</h3></div>", unsafe_allow_html=True)
pres_bins = pd.cut(pres_data['PRES'], bins=5)
pres_pie_data = pres_bins.value_counts().reset_index()
pres_pie_data.columns = ['Air Pressure Range', 'Count']  # Rename columns
fig, ax = plt.subplots()
ax.pie(pres_pie_data['Count'], labels=pres_pie_data['Air Pressure Range'], autopct='%1.1f%%')
st.pyplot(fig)

# Scatter Plot
st.markdown("<div class='card'><h3>Air Pressure Scatter Plot</h3></div>", unsafe_allow_html=True)
fig, ax = plt.subplots()
sns.scatterplot(x='timestamp', y='PRES', data=pres_data, ax=ax)
st.pyplot(fig)

st.markdown("<footer>Smart Agriculture Dashboard © 2024</footer>", unsafe_allow_html=True)
