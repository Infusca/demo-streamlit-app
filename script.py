import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Simple Data Dashboard')

upload_file = st.file_uploader('Choose a CSV file', type='csv') # widget provided by streamlit

if upload_file is not None:
    # st.write('File uploaded...')
    df = pd.read_csv(upload_file)
    
    st.subheader('Data Preview')
    st.write(df.head())
    
    st.subheader('Data Summary')
    st.write(df.describe())
    
    st.subheader('Filter Data')
    columns = df.columns.tolist()
    selected_col = st.selectbox('Select column to filer by', columns) # widget that gives dropdown list of values
    unique_values = df[selected_col].unique()
    selected_value = st.selectbox('Select value', unique_values)

    filtered_df = df[df[selected_col] == selected_value]
    st.write(filtered_df)
    
    st.subheader('Plot Data')
    x_col = st.selectbox('Select x-axis column', columns)
    y_col = st.selectbox('Select y-axis column', columns)
    
    if st.button('Generate Plot'):
        st.line_chart(filtered_df.set_index(x_col)[y_col])

else:
    st.write('Waiting on file upload...')