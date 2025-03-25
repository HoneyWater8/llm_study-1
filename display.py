import streamlit as st 

def print_message(role, message, is_streaming=False):
  with st.chat_message(role):
    if is_streaming:
      message_placeholder = st.empty()
      messages = ""
      for msg in message:
        messages += msg + " "
        message_placeholder.markdown(messages + " ")
    else:
      st.markdown(message)
      messages = message

  return messages

def print_history_message():
  # 이전 대화 내역을 화면에 표시
  for message in st.session_state.messages:
    print_message(message["role"], message["content"])


