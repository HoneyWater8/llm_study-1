import enum
import time
from openai import OpenAI
from groq import Groq

from common.llm.openai import OPENAI_LLMs
from common.llm.llama import GROQ_LLMs

class PROVIDER_TYPE(enum.Enum):
  # 제공자명 = (인덱스, 호출함수, 사용가능한 모델 리스트)
  groq = (enum.auto(), Groq, GROQ_LLMs)
  openai = (enum.auto(), OpenAI, OPENAI_LLMs)

def get_response_from_llm(choiced_provider:PROVIDER_TYPE, messages, llm_name:str):
  if not isinstance(choiced_provider, PROVIDER_TYPE):
    raise Exception("허락한 제공자가 아닙니다.") 
  elif llm_name not in choiced_provider.value[2].__members__:
    raise Exception("허락한 모델명이 아닙니다.") 

  # 전체 대화 내역 전달
  client = choiced_provider.value[1]()
  response = client.chat.completions.create(
    model=choiced_provider.value[2][llm_name].value[1],
    messages=messages,
    stream=True
  )

  for token in response:
    if token.choices[0].delta.content is not None:
      yield token.choices[0].delta.content
      time.sleep(0.05)








