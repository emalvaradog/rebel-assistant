# Imports
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain.schema import (AIMessage, HumanMessage, SystemMessage)
import os

# Setting up LLMs
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

chat = ChatOpenAI(streaming=True)

history = [SystemMessage(content="""Contexto inicial del agente""")]

def handle_conversation(user_input):
  # history.add_user_message(user_input)
  res = chat(st.session_state.messages).content
  # history.add_ai_message(res)
  return res

# Streamlit APP
st.header("ChatGPT Clone")

if "messages" not in st.session_state:
  st.session_state.messages = history

# GUI Chat messages
for message in st.session_state.messages:
  if isinstance(message, SystemMessage):
    continue
  elif isinstance(message, HumanMessage):
    with st.chat_message("user"):
      st.write(message.content)
  elif isinstance(message, AIMessage):
    with st.chat_message("rebel"):
      st.write(message.content)


user_input = st.chat_input(placeholder="En que te puedo ayudar?")

if user_input:
  with st.chat_message("user"):
    st.write(user_input)
  
  st.session_state.messages.append(HumanMessage(content=user_input))

  res = chat(st.session_state.messages).content

  with st.chat_message("rebel"):
    st.write(res)

  st.session_state.messages.append(AIMessage(content=res))
