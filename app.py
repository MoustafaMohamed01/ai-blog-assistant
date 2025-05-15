import streamlit at st

st.set_page_config(layout="wide")
st.title('Blog AI Assistant')
st.subheader('Now you can craft perfect blogs with the help of AI')

with st.sidebar:
    st.title('Input your blog details')
    st.subheader('Enter details of the blog you want to generate')

    blog_title = st.text_input('Blog Title')
    keywords = st.text_input('Keywords')

    num_words = st.slider('Number of words', min_value=200, max_value=2500, step=250)

    submit_button = st.button('Generate Blog')

