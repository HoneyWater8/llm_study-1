import streamlit as st 
from openai import OpenAI
import os

from history import init_history, add_history
from display import print_history_message, print_message
from input import get_prompt
from llm import get_response_from_llm, get_llm

##################################################
# 서비스 시작 
##################################################

os.environ['OPENAI_API_KEY'] = 'sk-'
st.title("Chatbot")

# 세션 상태 초기화
init_history() 
print_history_message()

# 사용자의 메세지 
prompt = get_prompt()

if prompt is not None:
    # 사용자 메시지를 세션 상태에 추가
    add_history({"role": "user", "content": prompt})
    
    # 사용자 메시지 표시
    print_message("user", prompt)
    
    # AI 응답을 세션 상태에 추가
    assistant_message = get_response_from_llm(get_llm(), st.session_state.messages)
    add_history({"role": "assistant", "content": assistant_message})    
    # AI 응답 표시
    print_message("assistant", assistant_message)

