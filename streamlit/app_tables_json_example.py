import  pandas as pd
import streamlit as st

st.title("Data playground")

st.subheader("Dataframe")
df = pd.DataFrame({
    "Name": ['Rahul', 'Ramu', 'Gokul', 'Raju', 'Steve', 'Jhon'],
    "Age": [10, 12, 14, 18, 17, 19],
    "Country": ["India", "China", "USA", "Japan", "Korea", "Australia"]
})

st.dataframe(df)

st.subheader("Static Table")

st.table(df)

st.subheader("Json Example")
data = {
    "Rahul": {"score": 20},
    "Ram": {"score": 35},
    "Gokul": {"score": 67}
}
st.json(data)