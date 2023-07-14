from . import openai_langchain as ol
import json

JSON_PATH='data/prompt.json'

#读取意图列表
def read_list():
    # 打开文件并读取数据
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

#组合提示词
def assemble_prompt(inten_list, question):
    prompt = f'请你依据意图列表判断以下内容所要表达的意图<{question}>，意图列表为这个json文件{inten_list}，回答的格式为”一级键-二级键“，如”写代码-生成streamlit界面”。如果内容中所表达的意图不再列表中，则回答：“我不知道”'
    print(prompt)
    return prompt

#判断意图,返回意图提示词
def judge(question):
    inten_list = read_list()
    prompt = assemble_prompt(inten_list, question)
    
    #print(prompt)
    intention = ol.llm_chat(prompt) 
    print("intention:", intention)
    if intention != "我不知道":
        inten1 = intention.split('-')[0]
        inten2 = intention.split('-')[1]
        with open(JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        #print(data[inten1][inten2])

        return 1, intention
    else:
        return 0, prompt

