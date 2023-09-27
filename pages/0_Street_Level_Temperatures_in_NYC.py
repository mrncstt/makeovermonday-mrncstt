import streamlit as st
import pandas as pd
import numpy as np
from urllib.error import URLError
import altair as alt
from streamlit.hello.utils import show_code

st.set_page_config(page_title="Street Level Temperatures NYC", page_icon="🌡️")

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.markdown("# Street Level Temperatures NYC")
st.sidebar.header("Street Level Temperatures NYC")
st.map(df)
