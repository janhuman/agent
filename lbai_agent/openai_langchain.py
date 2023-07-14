import os 
import openai
from langchain.llms import OpenAI
openai.api_key = "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"
# openai.api_base = "https://api.openai.com/v1"
openai.api_base = "https://api.laibutech.com/v1" 
os .environ[ "OPENAI_API_KEY" ] = "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"
os.environ["OPENAI_API_BASE"] = "https://api.laibutech.com/v1" 


def base_chat(message,model="gpt-3.5-turbo"):
    # gpt-3.5-turbo-0301     
    completion = openai.ChatCompletion.create(
      model=model, 
      messages=[
        {"role": "user", "content":message}
      ]
    )

    print(completion)    
    
    #print("completion.usage", completion.usage) 
    
    return completion.choices[0].message['content']

def llm_chat(text):
    # 初始化包装器，temperature越高结果越随机
    llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

    prompt = "请你扮演一个幽默的AI助理，用诙谐有趣的语气回复我的问题或者请求，内容如下<<<{}>>>".format(text)

    return llm(text)    