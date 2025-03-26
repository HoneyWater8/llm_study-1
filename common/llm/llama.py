import enum
import time
from groq import Groq

class GROQ_LLMs(enum.Enum):
  llama3 = (enum.auto(), "llama-3.3-70b-versatile") 
  qwen = (enum.auto(), "qwen-qwq-32b")

def ClientGROQ(
    model_name, messages:list[dict], stream=True
):
  
  client = Groq()
  response = client.chat.completions.create(
    model=GROQ_LLMs[model_name].value[1],
    messages=messages,
    stream=stream
  )

  for token in response:
    if token.choices[0].delta.content is not None:
      yield token.choices[0].delta.content
      time.sleep(0.05) 

