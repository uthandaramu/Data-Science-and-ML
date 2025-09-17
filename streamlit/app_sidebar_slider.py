import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris

st.sidebar.header("Filters")
option = st.sidebar.selectbox("Choose option", ["Option1", "Option2"])
st.sidebar.write("Selected:", option)

#Columns
col1, col2 = st.columns(2)

with col1:
    st.button("left button")

with col2:
    st.button("right button")

#state
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write("Counters:", st.session_state.count)

#slider
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

sepal_length = st.sidebar.slider("Sepal Length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
