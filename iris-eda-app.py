import streamlit as st 

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import os 
from PIL import Image, ImageEnhance, ImageFilter

""" A Simple Iris EDA App"""
st.title("Iris EDA App")
st.text("Built with Streamlit")

# Headers and Subheader
st.header("EDA App")
st.subheader("Iris Dataset")

# Videos 
vid_file = open("example.mp4", "rb").read()
st.video(vid_file)


# EDA 
my_dataset = './datasets/iris.csv'

# Fxn to Load Dataset
st.cache(persist=True)
def explore_data(dataset):
    df = pd.read_csv(os.path.join(dataset))
    return df

data = explore_data(my_dataset)

if st.checkbox("Preview Dataset"):
    if st.button("Head"):
        st.write(data.head())
    elif st.button("Tail"):
        st.write(data.tail())
    else:
        st.write(data.head(2))


# Show entire dataset
if st.checkbox("Show All Dataset"):
    st.write(data)

# Show Dimensions 
data_dim = st.radio("What Dimensions Do you want to se?", ("Rows", "Columns"))
if data_dim == 'Rows':
    st.text("Showing Rows")
    st.write(data.shape[0])
if data_dim == 'Columns':
    st.text("Showing Columns")
    st.write(data.shape[1])
else:
    st.text("Showing shape of Dataset")
    st.write(data.shape)

# Show Column Names 
if st.checkbox("Show Column Names"):
    st.write(data.columns)
    st.dataframe(data)

# Show Summary
if st.checkbox("Show Summary of Dataset"):
    st.write(data.describe())


# Select A column
col_option = st.selectbox("Select Column", ("sepal_length", "sepal_width", "petal_length", "petal_width", "species"))
if col_option == 'sepal_width':
    st.write(data['sepal_width'])
if col_option == 'sepal_length':
    st.write(data['sepal_length'])
if col_option == 'petal_width':
    st.write(data['petal_width'])
if col_option == 'petal_length':
    st.write(data['sepal_length'])
if col_option == 'species':
    st.write(data['species'])
else:
    st.write("Select Column")

# Plot
if st.checkbox("Show Bar Plot with Matplotlib"):
    st.write(data.plot(kind='bar'))
    st.pyplot()

# Correlation
if st.checkbox("Show Correlation Plot with Matplotlib"):
    st.write(plt.matshow(data.corr()))
    st.pyplot()

# Seaborn
if st.checkbox("Show Correlation Plot with Seaborn"):
    st.write(sns.heatmap(data.corr()))
    st.pyplot()

# Group
if st.checkbox("Show Bar Chart Plot"):
    v_group = data.groupby('species')
    st.bar_chart(v_group)
    st.pyplot()

# Line
if st.checkbox("Show Line Plot"):
    v_group = data.groupby('species')
    st.bar_chart(v_group)
    st.pyplot()

# Area
if st.checkbox("Show Area Plot"):
    v_group = data.groupby('species')
    st.area_chart(v_group)
    st.pyplot()



# Images
@st.cache
def load_image(img):
    im = Image.open(os.path.join(img))
    return im

species_type = st.radio("Select Species Type", ("setosa", "virginica", "versicolor"))
if species_type == 'setosa':
    st.text("Showing Setosa Species")
    st.image(load_image('imgs/iris_setosa.jpg'))
if species_type == 'virginica':
    st.text("Showing Virginica Species")
    st.image(load_image('imgs/iris_virginica.jpg'))
if species_type == 'versicolor':
    st.text("Showing Versicolor Species")
    st.image(load_image('imgs/iris_versicolor.jpg'))

# Show Image 
if st.checkbox("Show/Hide Image"):
    my_image = load_image('imgs/iris_setosa.jpg')
    enh = ImageEnhance.Contrast(my_image)
    num = st.slider("Set Image Contrast", 1.0, 4.0)
    img_width = st.slider("Set Image Width", 300, 500)
    st.image(enh.enhance(num), width=img_width)

# About
if st.button("About App"):
    st.text("Iris EDA App")
    st.text("Built with Streamlit")


