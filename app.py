import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getResponse(input_text, no_words, blog_style):
    """A Function to get the response from Llama 2"""
    llm = CTransformers(model='D:\Career\Projects\BlogGeneration\models\llama-2-7b-chat.ggmlv3.q8_0.bin')

st.set_page_config(page_title="Blog Generator", 
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generating Blogs using Llama 2")

input_text = st.text_input("Enter Blog Topic")

# Creating two columns for additional fields
col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("Number of Words")
with col2:
    blog_style = st.selectbox('Target Audience for Blog',
                              ('Researchers', 'Data Scientists', 'Common People'), 
                              index=0)
submit = st.button("Generate")

# Getting the final response
if submit:
    st.write(getResponse(input_text, no_words, blog_style))

