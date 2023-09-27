import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Set the page configuration
st.set_page_config(page_title="Street Level Temperatures NYC", page_icon="🌡️")

# Read the data from the provided URL
df = pd.read_json('https://data.cityofnewyork.us/resource/qdq3-9eqn.json')

# Display the column names to verify
st.write(df.columns.tolist())

# Rename columns to match previous naming convention
df = df.rename(columns={
    'AirTemp': 'airtemp',
    'Latitude': 'lat',
    'Longitude': 'lon',
    'Day': 'day'
})

# Extract and format the "day" column
df['day'] = df['day'].str[:10]
df['day'] = pd.to_datetime(df['day']).dt.strftime('%m-%d-%Y')

# Normalize the airtemp column to get values between 0 and 1 for heatmap intensity
max_temp = df['airtemp'].max()
min_temp = df['airtemp'].min()
df['airtemp_normalized'] = (df['airtemp'] - min_temp) / (max_temp - min_temp)

# Display the title and sidebar header
st.markdown("# Street Level Temperatures NYC")
st.sidebar.header("Street Level Temperatures NYC")

# Add a selector for the "day" column
selected_day = st.sidebar.selectbox("Select a Day:", df['day'].unique())

# Filter the dataframe based on the selected day
df_filtered = df[df['day'] == selected_day]

# Assuming 'lat' and 'lon' columns are present, proceed with the rest of the code
if 'lat' in df_filtered.columns and 'lon' in df_filtered.columns:
    # Plotting the heatmap
    layer = pdk.Layer(
        "HeatmapLayer",
        data=df_filtered,
        opacity=0.9,
        get_position=["lon", "lat"],
        get_weight="airtemp_normalized",
        threshold=0.3,
        radiusPixels=30,
    )

    view_state = pdk.ViewState(
        latitude=df_filtered['lat'].mean(),
        longitude=df_filtered['lon'].mean(),
        zoom=10,
        min_zoom=5,
        max_zoom=15,
        pitch=40.5,
        bearing=-27.36,
    )

    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

    # Optional: Display the raw data in a table below the map
    st.write(df_filtered)
