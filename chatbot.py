import streamlit as st 
from openai import OpenAI
import os

os.environ['OPENAI_API_KEY'] = 'sk-'
st.title("Chatbot")

# 세션 상태 초기화
# st.session_state 
# -> 딕셔너리 데이터
# -> st이 기억해야 하는 데이터들을 저장하는 곳  
if "messages" not in st.session_state: # session_state에 messages라는 키가 없다면, 
    # messages 이름으로 리스트 데이터 기억하기!
    st.session_state.messages = [] # 초기화!!! 


# 이전 대화 내역을 화면에 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자의 메세지 
prompt = st.chat_input("무엇이든지 물어봐주세요.")

if prompt is not None:
    # 사용자 메시지를 세션 상태에 추가
    st.session_state.messages.append(
        {"role": "user", "content": prompt})
    
    # 사용자 메시지 표시
    with st.chat_message("user"):
        st.markdown(prompt)
    
    client = OpenAI()
    
    # 전체 대화 내역을 OpenAI에 전달
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )
    
    # AI 응답을 세션 상태에 추가
    assistant_message = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
    
    # AI 응답 표시
    with st.chat_message("assistant"):
        st.markdown(response.choices[0].message.content)
