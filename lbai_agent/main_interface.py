import json
import streamlit as st
from . import openai_langchain as lc
from . import intention_judge as ij
from redis_utils import pub_sub
from lbai_agent.frame_change import write_config_to_file as change_congfig
from lbai_agent.code_manage import save_to_file, send_to_source
from lbai_agent import talk_to_agent
import subprocess

def run_talk_to_agent():
    file_path = r"C:\workplace\GPT_dev\lbai-agent1\lbai_agent\talk_to_agent.py"

    try:
        # 启动子进程运行命令
        subprocess.run(["python", file_path], check=True)
        #subprocess.run(["pwd"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"运行 {file_path} 失败：{e}")
    except FileNotFoundError:
        print(f"找不到 {file_path} 文件")



#更新session_state
def renew_session():

    # Initialize session states
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    if 'response' not in st.session_state:
        st.session_state.response = ""
    if 'code' not in st.session_state:
        st.session_state.code = "code"
    if 'show' not in st.session_state:
        st.session_state.show = {
            "聊天框":True,
            
        }    
renew_session()



def main():
    
    # Set page configuration
    st.set_page_config(page_title='来布智能体1.0', layout='wide')
    run_talk_to_agent()
    renew_session()
    st.session_state.user_input = ''
    #print("listen:", st.session_state.user_input)
    

    # Sidebar
    st.sidebar.title('资源库')
    input_text = st.sidebar.text_input('openai API-KEY')
    if st.sidebar.button('确认'):
        # Perform actions on button click
        pass
    
    options = ['编程工具', '控制', 'Option 3']
    selected_option = st.sidebar.selectbox('选择', options)

    tab1, tab2, tab3 = st.tabs(["主界面", "界面2", "界面3"])
    # Main

    col1, col2 = tab1.columns(2)
    #st.session_state.show["聊天框"] = False
    if st.session_state.show["聊天框"]:
        print(st.session_state.show)
        # Chat Interface
        col1.header('聊天')
        input_col, send_col = col1.columns((4,1))
        chat_input = input_col.text_input('和智能体对话', value=st.session_state.user_input)

        send_col.write("")
        send_col.write("")
        if send_col.button('发送'):
            # Store user input in session state
            st.session_state.user_input = chat_input
            
            # Call the answer function to get the response
        
        if st.session_state.user_input != '':
            answer(st.session_state.user_input)
        else:
            talk_input = talk_to_agent.read()
            if talk_input != None:
               st.session_state.user_input = talk_input
               answer(st.session_state.user_input) 
               talk_to_agent.clean()

       
            
    
    
        col1.text_area('', value=st.session_state.response, height=500)

    #功能栏
    function_area(col2, selected_option)


#生成回答
def answer(user_input):
    #renew_session()
    print(user_input)
    out_put = ''
    normal_flag, intention = ij.judge(user_input)
    if normal_flag == 0:
        out_put = lc.llm_chat("请你扮演一个幽默的机器人，你的名字叫做小布，请你回答我的提问"+user_input)
    #elif normal_flag == 1:
    elif normal_flag == 1:
            # 打开文件并读取数据

        inten1 = intention.split('-')[0]
        inten2 = intention.split('-')[1]
        
        if inten1 == '写代码':
            with open('data/prompt/code_p.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            st.session_state.code = ''
            st.session_state.code = lc.llm_chat(data[inten1][inten2]+user_input)
            
            redis_sub_info = intention
            write_data = save_to_file.extract_code_blocks(st.session_state.code)
            save_to_file.save_code(write_data)
            send_to_source.send()                        
            out_put = "小布现在帮你解决！"

        elif inten1 == "调整主界面" :

            if inten2 == "隐藏或者显示聊天界面":
                st.session_state.show["聊天框"] = not st.session_state.show["聊天框"]
                print(st.session_state.show)
                
                st.experimental_rerun() 

            else:
                #读取调整页面提示词
                with open('data/prompt/frame_p.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)            
                print("获取配置的提示词", data[inten1][inten2]+user_input)
                config_data = lc.llm_chat(data[inten1][inten2]+user_input)
                #print("config_data:", config_data)
                #更改主题配置
                change_congfig(config_data)
                out_put = "小布现在帮你解决！"

                #刷新使之生效
                st.experimental_rerun()  



    else:
        pass    

    # Your code to generate a response based on user input
    response = "Q: " + user_input + "\nA:" + out_put
    # Retrieve the existing chat history from session state
    chat_history = st.session_state.response
    # Append the new entry to the chat history
    chat_history += "\n" + response
    # Store the updated chat history in session state
    st.session_state.response = chat_history
    st.session_state.user_input = ''


#功能区
def function_area(col2, selected_option):

    # Custom Interface
    col2.header('功能区')
    if selected_option == '编程工具':
        col2.code(st.session_state.code)
    elif selected_option == '控制':
        col2.code('Code for Option 2')
    else:
        col2.code('Code for Option 3')

