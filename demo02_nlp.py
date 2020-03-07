import streamlit as st 

# NLP Pks 
import spacy
from textblob import TextBlob
from gensim.summarization import summarize
# Sumy Pkgs
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Summary Fxn 
def sumy_summarizer(docx):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarize = LexRankSummarizer()
    summary = lex_summarize(parser.document, 3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result


def text_analyzer(my_text):
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(my_text)
    for token in docx:
        print(token.text)
    tokens = [token.text for token in docx]
    allData = [('Tokens:{},\n Lemma: {}'.format(token.text, token.lemma_)) for token in docx]
    return allData

def entity_analyzer(my_text):
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(my_text)
    tokens = [token.text for token in docx]
    entities = [(entity.text, entity.label_) for entity in docx.ents]
    allData = ['"Tokens": {},\n"Entities": {}'.format(tokens, entities)]
    return allData


    

# Pks 


def main():
    """ NLP APP with Streamlit """
    st.title("NLPiffy with Streamlit")
    st.subheader("Natural Language Processing on the GO")

    # Tokanzaition

    # Tokenization
    if st.checkbox("Show Tokens and Lemma"):
        st.subheader("Tokenize Your Text")
        message = st.text_area("Enter You Text", "Type Here")
        if st.button("Analyze"):
            nlp_result = text_analyzer(message)
            st.json(nlp_result)

    # Named Entity
    if st.checkbox("Show Named Entities"):
        st.subheader("Show Named Entities")
        message = st.text_area("Enter You Text", "Python was created by Guido. He Works in UK")
        if st.button("Extract"):
            nlp_result = entity_analyzer(message)
            st.json(nlp_result)

    # Sentiment Analysis
    if st.checkbox("Show Sentiment Analysis"):
        st.subheader("Show Named Entities")
        message = st.text_area("Enter You Text", "He loves reading and cooking.")
        if st.button("Analyze"):
            blob = TextBlob(message)
            result_sentiment = blob.sentiment
            st.success(result_sentiment)


    # Text Summalization
    if st.checkbox("Show Text Summarization"):
        st.subheader("Show Named Entities")
        message = st.text_area("Enter You Text", "He loves reading and cooking.\nHe is a programmer.")
        summary_options = st.selectbox("Choice Your Summarize", ("gensim", "sumy"))        
        if st.button("Summarize"):
            if summary_options == 'gensim':
                st.text("Using Gensim..")
                summary_result = summarize(message)
            elif summary_options == 'sumy':
                import nltk; nltk.download('punkt')
                st.text("Using Sumy..")
                summary_result = sumy_summarizer(message)
            else:
                st.warning("Using Defult Summarizer")
                st.text("Using Gensim")
                summary_result = summarize(message)
            st.success(summary_result)
            

            

    # Sentiment Analysis


    # Text Summarization





if __name__ == '__main__':
    main()