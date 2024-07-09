import streamlit as st
import os
import textwrap
from dotenv import load_dotenv
import google.generativeai as genai
from IPython.display import display, Markdown


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title="Q&A Demo", page_icon=":network:", layout="wide")


st.markdown(
    """
    <style>
    .main {
        background-color: #EEF7FF; 
        padding: 10px;
    }
    .stButton>button {
        color: white;
        background-color: #5AB2FF; 
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        color: white;
        background-color: #0277BD;  
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 10px;
        border: 2px solid #0288D1;
    }
    .stHeader {
        color: #0288D1;  
    }
    .stSubheader {
        color: #000000;  
    }
    .stMarkdown {
        color: #000000;  
    }
   
    </style>
    
    """,
    unsafe_allow_html=True
)


st.header("Network  Optimisation Techniques")


input_question = st.text_input("Ask question: ", key="input")


submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input_question)
    st.subheader("Find your solution")
    st.write(response)
