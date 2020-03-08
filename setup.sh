mkdir -p ~/.streamlit/

pip install --upgrade pip

echo "\
[server]\n\
headless=true\n\
port=$PORT\n\
enableCORS=false\n\
\n\
" > ~/.streamlit/config.toml