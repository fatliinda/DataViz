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

# Filter for Soil Moisture (SOIL1)
soil_data = data[['timestamp', 'SOIL1']]

# Page title
st.title("Soil Moisture (SOIL1) Visualizations")

# Line Chart
st.markdown("<div class='card'><h3>Soil Moisture Over Time</h3></div>", unsafe_allow_html=True)
st.line_chart(soil_data.set_index('timestamp')['SOIL1'])

# Bar Chart
st.markdown("<div class='card'><h3>Soil Moisture Distribution</h3></div>", unsafe_allow_html=True)
st.bar_chart(soil_data.set_index('timestamp')['SOIL1'])

# Pie Chart
st.markdown("<div class='card'><h3>Soil Moisture Proportions</h3></div>", unsafe_allow_html=True)
soil_bins = pd.cut(soil_data['SOIL1'], bins=5)
soil_pie_data = soil_bins.value_counts().reset_index()
soil_pie_data.columns = ['Soil Moisture Range', 'Count']  # Rename columns
fig, ax = plt.subplots()
ax.pie(soil_pie_data['Count'], labels=soil_pie_data['Soil Moisture Range'], autopct='%1.1f%%')
st.pyplot(fig)

# Scatter Plot
st.markdown("<div class='card'><h3>Soil Moisture Scatter Plot</h3></div>", unsafe_allow_html=True)
fig, ax = plt.subplots()
sns.scatterplot(x='timestamp', y='SOIL1', data=soil_data, ax=ax)
st.pyplot(fig)

st.markdown("<footer>Smart Agriculture Dashboard © 2024</footer>", unsafe_allow_html=True)
