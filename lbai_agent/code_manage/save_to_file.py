import json
import subprocess
import random
import psutil



#将代码保存为文件
def save_code(code):
    id = generate_random_number()
    filename = 'created_code.py'

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(code)
    return filename


#生成随机数
def generate_random_number(start=0, end=1000):
    """
    生成指定范围内的随机整数

    参数:
        start (int): 范围的起始值
        end (int): 范围的结束值

    返回值:
        int: 在指定范围内生成的随机整数
    """
    return random.randint(start, end)


#去除代码块格式
def extract_code_blocks(anwser, language='python'):
    if language == 'streamlit':
        language = 'python'
    anwser = anwser.split('```{}'.format(language))[-1]
    anwser = anwser.split('```')[0]
    return anwser


