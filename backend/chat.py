# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model a nd get respones
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response =chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")


if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]


input=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")



## If ask button is clicked

if submit and input:
    
    response=get_gemini_response(input)
    st.session_state['chat_history'].append(("You",input))

    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("Chat history is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
        #print(st.write(chunk.text))
        print("_"*80)
    
    st.write(chat.history)
