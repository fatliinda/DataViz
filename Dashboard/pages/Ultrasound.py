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

# Filter for Ultrasound (US)
us_data = data[['timestamp', 'US']]

# Page title
st.title("Ultrasound (US) Visualizations")

# Line Chart
st.markdown("<div class='card'><h3>Ultrasound Over Time</h3></div>", unsafe_allow_html=True)
st.line_chart(us_data.set_index('timestamp')['US'])

# Bar Chart
st.markdown("<div class='card'><h3>Ultrasound Distribution</h3></div>", unsafe_allow_html=True)
st.bar_chart(us_data.set_index('timestamp')['US'])

# Pie Chart
st.markdown("<div class='card'><h3>Ultrasound Proportions</h3></div>", unsafe_allow_html=True)
us_bins = pd.cut(us_data['US'], bins=5)
us_pie_data = us_bins.value_counts().reset_index()
us_pie_data.columns = ['Ultrasound Range', 'Count']  # Rename columns
fig, ax = plt.subplots()
ax.pie(us_pie_data['Count'], labels=us_pie_data['Ultrasound Range'], autopct='%1.1f%%')
st.pyplot(fig)

# Scatter Plot
st.markdown("<div class='card'><h3>Ultrasound Scatter Plot</h3></div>", unsafe_allow_html=True)
fig, ax = plt.subplots()
sns.scatterplot(x='timestamp', y='US', data=us_data, ax=ax)
st.pyplot(fig)

st.markdown("<footer>Smart Agriculture Dashboard © 2024</footer>", unsafe_allow_html=True)
