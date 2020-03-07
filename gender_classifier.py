import streamlit as st 

# ML Pkgs 
import joblib
from PIL import Image

# Vectorizer
gender_vectorizer = open("models/gender_vectorizer.pkl", "rb")
gender_cv = joblib.load(gender_vectorizer)

# Models
gender_nv_model = open("models/naivebayesgendermodel.pkl", "rb")
gender_clf = joblib.load(gender_nv_model)

def predict_gender(data):
    vect = gender_cv.transform(data).toarray()
    result = gender_clf.predict(vect)
    return result

def load_images(image_name):
    img = Image.open(image_name)
    return st.image(img, width=300)

def load_css(css_file):
    with open(css_file) as f:
        st.markdown('<stule>{}</style>'.format(f.read()), unsafe_allow_html=True)

def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)

""" Gender Classifer APP"""
st.title("Gender Calssifier ML App")
st.subheader("With Streamlit")

load_css('icon.css')
# load_icon('people')

name = st.text_input("Enter Name", "Type Here")
if st.button("Classify"):
    st.text("Name {}".format(name.title()))
    result = predict_gender([name.title()])    
    if result[0] == 0:
        prediction = 'Female'
        c_image = 'female.png'        
    else:
        prediction = 'Male'
        c_image = 'male.png'
    st.success("Name {}, was classified as {}".format(name.title(), prediction))
    load_images('./images/' + c_image)