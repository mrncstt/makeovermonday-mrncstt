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
    'Longitude': 'lon'
})

# Normalize the airtemp column to get values between 0 and 1 for heatmap intensity
max_temp = df['airtemp'].max()
min_temp = df['airtemp'].min()
df['airtemp_normalized'] = (df['airtemp'] - min_temp) / (max_temp - min_temp)

# Display the title and sidebar header
st.markdown("# Street Level Temperatures NYC")
st.sidebar.header("Street Level Temperatures NYC")

# Display the map with heatmap
st.map(df, zoom=10)

# Optional: Display the raw data in a table below the map
st.write(df)

if __name__ == '__main__':
    st.write("Streamlit App is running!")
