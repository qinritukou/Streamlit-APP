# Streamlit-APP
stream lit app demo

# Required files
1. setup.sh
2. Procfile
3. requirements.txt
    'pipenv run pip freeze > requirements.txt'


# Tools used
1. pipenv


# memo

### install package 
    pipenv install streamlit
    pipenv install shell
    pipenv install WordCloud
    pipenv run python3 -m spacy download en_core_web_sm


### run 
    pipenv run streamlit run iris-eda-app.py

### heroku
    heroku login
    heroku create <app-name>
    