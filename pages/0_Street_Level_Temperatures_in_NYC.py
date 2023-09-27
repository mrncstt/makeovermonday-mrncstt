import streamlit as st
import pandas as pd
import numpy as np

# Set the page configuration
st.set_page_config(page_title="Street Level Temperatures NYC", page_icon="🌡️")

# Read the data from the provided URL
df = pd.read_json('https://data.cityofnewyork.us/resource/qdq3-9eqn.json')

# Rename columns to match previous naming convention
df = df.rename(columns={
    'AirTemp': 'airtemp',
    'Latitude': 'lat',
    'Longitude': 'lon',
    'Day': 'day'
})

# Extract and format the "Day" column
df['day'] = df['day'].str[:10]
df['day'] = pd.to_datetime(df['Day']).dt.strftime('%m-%d-%Y')

# Normalize the airtemp column to get values between 0 and 1 for heatmap intensity
max_temp = df['airtemp'].max()
min_temp = df['airtemp'].min()
df['airtemp_normalized'] = (df['airtemp'] - min_temp) / (max_temp - min_temp)

# Display the title and sidebar header
st.markdown("# Street Level Temperatures NYC")
st.sidebar.header("Street Level Temperatures NYC")

# Add a selector for the "Day" column
selected_day = st.sidebar.selectbox("Select a Day:", df['Day'].unique())

# Filter the dataframe based on the selected day
df_filtered = df[df['Day'] == selected_day]

# Display the map with heatmap for the selected day
st.map(df_filtered, zoom=10)

# Optional: Display the raw data in a table below the map
st.write(df_filtered)


