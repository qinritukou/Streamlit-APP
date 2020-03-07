import streamlit as st 

st.title("Streamlit Tutorials")

st.header("This is a header")
st.subheader("This is a subheader")

st.text("Hello Streamlit")

st.markdown("### This is a Markdown")

st.success("Successful")

st.info("Information!")

st.warning("This is a warning")

st.error("This is an error Danger")

st.exception("NameErr('name three not defined')")

# Get Help Info About Python
st.help(range)

# Write Text 
st.write("Text with write")

st.write(range(10))

# Images 
# from PIL import Image
# img = Image.open("example.jpg")
# st.image(img, width=300, caption="Simple Image")


# Videos 
# vid_file = open("example.mp4", "rb").read()
# st.video(vid_file)

# Audio
# audio_file = open("example.mp3", "rb").read()
# st.audio(audio_file, format='audio/mp3')


# Wdiget 
# Checkbox 
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")


# Radio 
status = st.radio("What is your status", ("Active", "Inactive"))
if status == 'Active':
    st.success("You are Active")
else:
    st.warning("Inactive")

# SelectBox
occupation = st.selectbox("Your Occupation", ["Programmer", "Doctor", "Lawyer"])
st.write("You selected this option", occupation)


# MultiSelect 
location = st.multiselect("Where do you work?", ("London", "New York", "Tokyo"))
st.write(location)


# Slider 
level = st.slider("What is your level", 1, 5)
st.write(level)

# Buttons 
st.button("Simple Button")

if st.button("About"):
    st.text("Streamlit is Cool")

# Text Input 
firstname = st.text_area("Enter Your Firstname", "Type Here...")
if st.button("Submit"):
    result = firstname.title()
    st.success(result)

# Date Input
import datetime
today = st.date_input("Today is", datetime.datetime.now())
st.write(today)

# Time
the_time = st.time_input("The time is", datetime.time())
st.write(the_time)


# Display JSON
st.text("Display JSON")
st.json({
    'name': 'Jesse',
    'gender': 'male'
})

# Display Raw Data
st.text("Display Raw Code")
st.code("improt numpy as np")


# Display Raw Code 
with st.echo():
    # This will also show as a comment 
    import pandas as pd 
    df = pd.DataFrame()

# Progress Bar
import time 
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

# Spinner 
with st.spinner("Waiting ..."):
    time.sleep(5)
st.success("Finished!")

# Balloons
# st.balloons()


# SIDEBARS
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tutorial")


# Functions
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())


# Plot
df = pd.read_csv("titanic.csv", sep='\t')
st.pyplot()

# DataFrames
st.dataframe(df)

# Tables 
st.table(df)