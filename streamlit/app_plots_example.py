import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(30, 3),columns=['a', 'b', 'c'])

st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Bar plot")
st.bar_chart(chart_data)

st.subheader("Map")
map_data = pd.DataFrame(np.random.randn(100, 2)/[50, 50]+[37.37, -112.2], columns=["lat", "lon"])
st.map(map_data)