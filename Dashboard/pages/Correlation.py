import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load custom CSS (assuming your CSS file is named "styles.css")
with open("styles.css") as f:
  st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the data from the CSV file
data = pd.read_csv("./cleaned_data.csv")
data["timestamp"] = pd.to_datetime(data["timestamp"])

# Calculate the correlation matrix
corr_matrix = data[["TC", "HUM", "PRES", "US", "SOIL1"]].corr()

# Function to explain correlation strength
def explain_correlation(corr_value):
  """
  Provides a text explanation based on the correlation coefficient value.
  """
  if abs(corr_value) < 0.2:
    return "Very weak or no correlation."
  elif abs(corr_value) <= 0.4:
    return "Weak correlation."
  elif abs(corr_value) <= 0.6:
    return "Moderate correlation."
  elif abs(corr_value) <= 0.8:
    return "Strong correlation."
  else:
    return "Very strong correlation."

# Function to display the full correlation matrix heatmap
def show_full_heatmap():
  """
  Displays the heatmap for the entire correlation matrix.
  """
  fig, ax = plt.subplots()
  sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax, linewidths=0.5)
  ax.set_title("Correlation Matrix (All Factors)")
  st.pyplot(fig)

# Page title
st.title("Correlation Analyzer for Environmental Factors")

# User Input for selecting factors
factor1 = st.selectbox("Select First Factor:", ["TC", "HUM", "PRES", "US", "SOIL1"])
factor2 = st.selectbox("Select Second Factor:", ["TC", "HUM", "PRES", "US", "SOIL1"])

# Buttons for correlation analysis and full matrix display
if st.button("Calculate Correlation"):

  # Check if user selected factors
  if factor1 != factor2 and factor1 is not None and factor2 is not None:
    # Get correlation coefficient
    corr_value = corr_matrix.loc[factor1, factor2]

    # Display correlation heatmap (reduced size for better layout)
    fig, ax = plt.subplots(figsize=(5, 5))
    sns.heatmap(corr_matrix[[factor1, factor2]][[factor1, factor2]], annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    ax.set_title("Correlation Heatmap (Selected Factors)")
    st.pyplot(fig)

    # Display correlation value and explanation
    st.write(f"**Correlation between {factor1} and {factor2}:** {corr_value:.2f}")
    st.write(explain_correlation(corr_value))
  else:
    st.warning("Please select two different factors to calculate correlation.")

if st.button("Show All"):
  show_full_heatmap()

# Footer
st.markdown("<footer>Smart Agriculture Dashboard © 2024</footer>", unsafe_allow_html=True)
