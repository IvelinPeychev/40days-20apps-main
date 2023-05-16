import streamlit as st
import pandas

st.set_page_config(page_title='Home', layout='wide')

# st.sidebar.title('Home')
# st.sidebar.title('Contact me')

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.png")

with col2:
    st.title("Ivelin Peychev")
    content = """
    Hi! My name is Ivelin and this is my first Python development project. I am a Senior QA but I fond of 
    learning Python and programming with it. My goal is to become an active programmer, automation QA and 
    penetration ethical hacker.
    """
    # st.write(content)
    st.info(content)

# With .header we can place header for the category, not wrong but .write is the teacher's solution
# st.header('Below you can find some of the apps I have build with Python. Feel free to contact me at any time!')
content2 = """
Below you can find some of the apps I have build with Python. Feel free to contact me at any time!
"""
st.write(content2)


df = pandas.read_csv('data.csv', sep=';')

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    # Iterate the data file and extract the titles by using iterrows method
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row["url"]})')