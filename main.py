import streamlit as st

#st.write("hello")
#st.write({"key": ["value"]})

import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Dashboard")
fileup=st.file_uploader("Choose a file", type="csv")

if fileup is not None:
    #st.write("file uploaded..")
    df = pd.read_csv(fileup)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader('Data Summary')
    st.write(df.describe())


    st.subheader('Filter Data')
    columns = df.columns.tolist()
    selected_column = st.selectbox("select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("plot Data")
    x_col = st.selectbox("select x column", columns)
    y_col = st.selectbox("select y column", columns)
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_col)[y_col])
else:
    st.write("WAiting For File To Be Uploaded..")