import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello world")
#st.text_input("Favorite color")
x=st.text_input("Favourite color")
st.write(f"your Favorite color is:{x}")

st.write(f"Your colour is: {x}")


# import file logic

data=pd.read_csv("movies.csv")
st.write(data)
st.header("#My Nilesh's Cool Chart")

chart_data=pd.DataFrame(
    np.random.randn(20,3),
columns=["a","b","c"]
    )
st.bar_chart(chart_data)
st.line_chart(chart_data)
st.button("Name")

