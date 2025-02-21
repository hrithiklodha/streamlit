#streamlit app with various widgets for a user to interact with
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Title
st.title('Streamlit App')

# Header
st.header('This is a header')
st.subheader('This is a subheader')

# Text
st.text('Hello Streamlit')

# Markdown
st.markdown('### This is a markdown')

# Error/Colorful Text
st.error('This is an error')
st.warning('This is a warning')
st.info('This is an info')
st.success('This is a success')

# Write
st.write('This is a write')

# Dataframe
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Doe'],
    'age': [25, 30, 35]
})
st.write(df)

# Button
if st.button('Click me'):
    st.write('Button clicked')
    
# Checkbox
if st.checkbox('Show/Hide'):
    st.write('Checkbox clicked')
    
# Radio
status = st.radio('What is your status?', ('Active', 'Inactive'))
if status == 'Active':
    st.write('You are active')
else:
    st.write('You are inactive')
    
# Selectbox
occupation = st.selectbox('What is your occupation?', ['Programmer', 'Data Scientist', 'Doctor'])
st.write(f'You selected: {occupation}')

# Multiselect
location = st.multiselect('Where do you work?', ['New York', 'San Francisco', 'Los Angeles'])
st.write(f'You selected: {location}')

# Slider
level = st.slider('What is your level?', 1, 5)
st.write(f'You selected: {level}')

# Text Input
name = st.text_input('Enter your name')
st.write(f'Your name is: {name}')

# Number Input
age = st.number_input('Enter your age')
st.write(f'Your age is: {age}')

# Text Area
message = st.text_area('Enter your message')
st.write(f'Your message is: {message}')

# Date Input
date = st.date_input('Enter a date')
st.write(f'You selected: {date}')

# Time Input
time = st.time_input('Enter a time')
st.write(f'You selected: {time}')

# File Uploader
file = st.file_uploader('Upload a file', type=['csv', 'txt'])
if file is not None:
    st.write(file)
    
# Color Picker
color = st.color_picker('Pick a color', '#00f900')
st.write(f'You picked: {color}')

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(100):
    time.sleep(0.1)
    my_bar.progress(p + 1)
    
# Spinner
with st.spinner('Waiting...'):
    time.sleep(5)
    st.success('Done')
    
# Balloons
st.balloons()

# Plot
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})
st.line_chart(df)

