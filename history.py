import streamlit as st 


# 히스토리 초기화 
def init_history():
  # 세션 상태 초기화
  # st.session_state 
  # -> 딕셔너리 데이터
  # -> st이 기억해야 하는 데이터들을 저장하는 곳  
  if "messages" not in st.session_state: # session_state에 messages라는 키가 없다면, 
    # messages 이름으로 리스트 데이터 기억하기!
    st.session_state.messages = [] # 초기화!!! 

# 사용자 & AI message 추가 
def add_history(message:dict):
  st.session_state.messages.append(message)
