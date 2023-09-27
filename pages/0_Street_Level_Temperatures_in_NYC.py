import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)


st.set_page_config(page_title="Street Level Temperatures NYC", page_icon="🌡️")
st.markdown("# Street Level Temperatures NYC")
st.sidebar.header("Street Level Temperatures NYC")
st.write(

)

animation_demo()

show_code(animation_demo)
