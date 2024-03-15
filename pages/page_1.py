import requests
import streamlit as st

api_token = st.secrets.GIPHY.api

url = 'https://api.giphy.com/v1/gifs/random'

col1, col2, col3 = st.columns(3)

with col1:

    gif = st.text_input('Please, select the giphy you want...', 'dog')

    params = {'api_key':api_token, 'tag':gif}

    response = requests.get(url, params=params).json()

    giphy = response['data']['embed_url']

    st.write(f"<iframe src={giphy}>", unsafe_allow_html=True)

with col2:

    gif = st.text_input('Please, select the giphy you want...', 'cat')

    params = {'api_key':api_token, 'tag':gif}

    response = requests.get(url, params=params).json()

    giphy = response['data']['embed_url']

    st.write(f"<iframe src={giphy}>", unsafe_allow_html=True)

with col3:

    gif = st.text_input('Please, select the giphy you want...', 'bird')

    params = {'api_key':api_token, 'tag':gif}

    response = requests.get(url, params=params).json()

    giphy = response['data']['embed_url']

    st.write(f"<iframe src={giphy}>", unsafe_allow_html=True)
