import streamlit as st
from openai import OpenAI

def get_llm():
  return OpenAI()

def get_response_from_llm(llm, messages, llm_name="gpt-4o-mini"):
  # 전체 대화 내역을 OpenAI에 전달
  response = llm.chat.completions.create(
      model=llm_name,
      messages=messages
  )

  return response.choices[0].message.content

