import streamlit as st 
import joblib, os 


import spacy
nlp = spacy.load('en_core_web_sm')

# EDA 
import pandas as pd
import matplotlib.pyplot as plt

# Wordcloud 
from wordcloud import WordCloud
from PIL import Image 


# WordCount
news_vectorizer = open("models/final_news_cv_vectorizer.pkl", "rb")
news_cv = joblib.load(news_vectorizer)

# Load Our Models
def load_prediction_models(model_file):
    loaded_models = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_models

def get_keys(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key



st.title("News Classifier App")
st.subheader("NLP and ML App with Streamlit")

activities = ["Prediction", "NLP"]
choice = st.sidebar.selectbox("Choose Activity", activities)
if choice == 'Prediction':
    st.info("Prediction with ML")
    news_text = st.text_area("Enter Text", "Type here")
    all_ml_models = ["LR", "NB", "RFOREST", "DECISION_TREE"]
    model_choice = st.selectbox("Choose ML Model", all_ml_models)
    prediction_labels = { 'business': 0, 'tech': 1, 'sport': 2, 'health': 3, 'politics': 4, 'entertainment': 5 }
    if st.button("Classify"):
        st.text("Original test ::\n{}".format(news_text))
        vect_text = news_cv.transform([news_text]).toarray()
        if model_choice == 'LR':
            predictor = load_prediction_models("models/newsclassifier_Logit_model.pkl")
            prediction = predictor.predict(vect_text)

        if model_choice == 'RFOREST':
            predictor = load_prediction_models("models/newsclassifier_RFOREST_model.pkl")
            prediction = predictor.predict(vect_text)

        if model_choice == 'NB':
            predictor = load_prediction_models("models/newsclassifier_NB_model.pkl")
            prediction = predictor.predict(vect_text)
            
            
        if model_choice == 'DECISION_TREE':
            predictor = load_prediction_models("models/newsclassifier_CART_model.pkl")
            prediction = predictor.predict(vect_text)

        final_result = get_keys(prediction, prediction_labels)
        st.info(final_result)



if choice == 'NLP':
    st.info("Natural Language Processing")
    news_text = st.text_area("Enter Text", "Type Here")
    nlp_task = ["Tokenization", "NER", "Lemmatization", "POS Tags"]
    task_choice = st.selectbox("Choose NLP Task", nlp_task)

    if st.button("Analyze"):
        st.info("Original Text:\n{}".format(news_text))

        docx = nlp(news_text)
        if task_choice == 'Tokenization':
            result = [ token.text for token in docx ]
        if task_choice == 'NER':
            result = [(entity.text, entity.label) for entity in docx.ents]
        if task_choice == 'POS Tags':
            result = ["'Token':{}, 'POS': {}, 'Dependency': {}".format(word.text, word.tag_, word.dep_) for word in docx]
        
        st.json(result)
    
    if st.button("Tabulize"):
        docx = nlp(news_text)
        c_tokens = [ token.text for token in docx ]
        c_lemma = [(token.text, token.lemma_) for token in docx]
        c_pos = [(word.text, word.tag_, word.dep_) for word in docx]

        new_df = pd.DataFrame(zip(c_tokens, c_lemma, c_pos), columns=['Tokens', 'Lemma', 'POS'])
        st.dataframe(new_df)

    if st.checkbox("Wordcloud"):
        wordcloud = WordCloud().generate(news_text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot()