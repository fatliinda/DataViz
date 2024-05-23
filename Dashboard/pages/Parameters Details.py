import streamlit as st
import pandas as pd

# Load custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the data
data = pd.read_csv('./cleaned_data.csv')

# Convert timestamp column to datetime
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Sidebar for date selection
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", data['timestamp'].min())
end_date = st.sidebar.date_input("End Date", data['timestamp'].max())

# Check if the start and end dates are the same
if start_date == end_date:
    st.sidebar.write("Select hours for the same day:")
    start_time = st.sidebar.time_input("Start Time", pd.to_datetime(data['timestamp']).min().time())
    end_time = st.sidebar.time_input("End Time", pd.to_datetime(data['timestamp']).max().time())
else:
    start_time = pd.to_datetime(data['timestamp']).min().time()
    end_time = pd.to_datetime(data['timestamp']).max().time()

# Sidebar for parameter selection
parameter_dict = {
    "TC": "Temperature",
    "HUM": "Humidity",
    "PRES": "Air Pressure",
    "US": "Ultrasound",
    "SOIL1": "Soil Moisture"
}
parameter = st.sidebar.selectbox("Parameter", list(parameter_dict.keys()), format_func=lambda x: parameter_dict[x])

# Filter data based on date and time selection
if start_date == end_date:
    filtered_data = data[
        (data['timestamp'] >= pd.to_datetime(f"{start_date} {start_time}")) &
        (data['timestamp'] <= pd.to_datetime(f"{end_date} {end_time}"))
    ]
else:
    filtered_data = data[
        (data['timestamp'] >= pd.to_datetime(f"{start_date} {start_time}")) &
        (data['timestamp'] <= pd.to_datetime(f"{end_date} {end_time}"))
    ]

# Display filtered data
st.markdown(f"<div class='main'><h2>{parameter_dict[parameter]} Data from {start_date} to {end_date}</h2></div>", unsafe_allow_html=True)
st.line_chart(filtered_data.set_index('timestamp')[parameter])

# Display min and max values
min_value = filtered_data[parameter].min()
max_value = filtered_data[parameter].max()
st.markdown(f"<div class='card'><p>Min {parameter_dict[parameter]}: {min_value}</p><p>Max {parameter_dict[parameter]}: {max_value}</p></div>", unsafe_allow_html=True)

st.markdown("<footer>Smart Agriculture Dashboard © 2024</footer>", unsafe_allow_html=True)
