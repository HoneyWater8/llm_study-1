import enum
import time
from openai import OpenAI
from groq import Groq

from common.llm.openai import OPENAI_LLMs, Provider_OPENAI
from common.llm.llama import GROQ_LLMs, Provider_GROQ
from common.llm.ollama import OLLAMA_LLMs, Provider_OLLMA

class Provider:
  def __init__(self, provider_LLMs:enum.Enum):
    self.provider_LLMs = provider_LLMs # provider가 제공하는 모델 리스트

  def __call__(self, model_name, messages):
    pass

  def get_generator_from_llm(self, choiced_provider, messages, llm_name:str):
    pass


class PROVIDER_TYPE(enum.Enum):
  # 제공자명 = (인덱스, 호출함수, 사용가능한 모델 리스트)
  groq = (enum.auto(), Provider_GROQ, GROQ_LLMs)
  openai = (enum.auto(), Provider_OPENAI, OPENAI_LLMs)
  ollama = (enum.auto(), Provider_OLLMA, OLLAMA_LLMs)


def get_response_from_llm(choiced_provider:Provider, messages, llm_name:str):
  if not isinstance(choiced_provider, Provider):
    raise Exception("허락한 제공자가 아닙니다.") 
  elif llm_name not in choiced_provider.provider_LLMs:
    raise Exception("허락한 모델명이 아닙니다.") 

  generator = choiced_provider(
    model_name=llm_name, messages=messages
  )

  for token in choiced_provider.value[1](
    model_name=llm_name, messages=messages
  ):
    yield token
    time.sleep(0.05) 








