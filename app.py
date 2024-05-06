import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

def getResponse(input_text, no_words, blog_style):
    """A Function to get the response from Llama 2"""

    # Declaring the model
    # Download the model from HuggingFace, place it in a folder, and copy paste the path in place of the path here
    llm = CTransformers(model = 'models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = "llama",
                        config = {'max_new_tokens':256,
                                'temperature':0.01})
    
    # Prompt template
    template = """
    Write a blog for {blog_style} job profile for a topic {input_text} within {no_words}.
            """
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template=template)
    
    # Generating the response from Llama 2
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)

    return response


st.set_page_config(page_title="Blog Generator", 
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Blog Generator")

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

