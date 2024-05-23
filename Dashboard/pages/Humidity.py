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

# Filter for Humidity (HUM)
hum_data = data[['timestamp', 'HUM']]

# Page title
st.title("Humidity (HUM) Visualizations")

# Line Chart
st.markdown("<div class='card'><h3>Humidity Over Time</h3></div>", unsafe_allow_html=True)
st.line_chart(hum_data.set_index('timestamp')['HUM'])

# Bar Chart
st.markdown("<div class='card'><h3>Humidity Distribution</h3></div>", unsafe_allow_html=True)
st.bar_chart(hum_data.set_index('timestamp')['HUM'])

# Pie Chart
st.markdown("<div class='card'><h3>Humidity Proportions</h3></div>", unsafe_allow_html=True)
hum_bins = pd.cut(hum_data['HUM'], bins=5)
hum_pie_data = hum_bins.value_counts().reset_index()
hum_pie_data.columns = ['Humidity Range', 'Count']  # Rename columns
fig, ax = plt.subplots()
ax.pie(hum_pie_data['Count'], labels=hum_pie_data['Humidity Range'], autopct='%1.1f%%')
st.pyplot(fig)

# Scatter Plot
st.markdown("<div class='card'><h3>Humidity Scatter Plot</h3></div>", unsafe_allow_html=True)
fig, ax = plt.subplots()
sns.scatterplot(x='timestamp', y='HUM', data=hum_data, ax=ax)
st.pyplot(fig)

st.markdown("<footer>Smart Agriculture Dashboard © 2024</footer>", unsafe_allow_html=True)
