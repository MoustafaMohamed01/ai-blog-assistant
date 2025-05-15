import streamlit as st
import google.generativeai as genai
from api_key import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

generation_config = {
    'temperature': 0.9,
    'top_p': 1,
    'top_k': 1,
    'max_output_tokens': 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

model = genai.GenerativeModel(model_name='gemini-2.0-flash',
                              generation_config=generation_config,
                              safety_settings=safety_settings)


st.set_page_config(layout="wide")
st.title('Blog AI Assistant')
st.subheader('Now you can craft perfect blogs with the help of AI')

with st.sidebar:
    st.title('Input your blog details')
    st.subheader('Enter details of the blog you want to generate')

    blog_title = st.text_input('Blog Title')
    keywords = st.text_input('Keywords')

    num_words = st.slider('Number of words', min_value=200, max_value=2500, step=250)

    prompt_parts = [f'Generate a comprehensive, engaging blog post relevant to the given title: "{blog_title}" and keywords: "{keywords}". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words.']
    response = model.generate_content(prompt_parts)

    submit_button = st.button('Generate Blog')


if submit_button:
    st.write(response.text)
