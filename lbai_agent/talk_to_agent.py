import redis_utils.pub_sub as pub_sub
import streamlit as st

def listen():
    def show_sub(channel, data):
        file_path = "talk.txt"

        with open(file_path, "a") as file:
            file.write(data + "\n")

        print(f"收到消息：{data}")
        #st.experimental_rerun() 

    pub_sub.subscribe_channel("1", show_sub)



def read():
    file_path = "talk.txt"
    
    with open(file_path, "r") as file:
        content = file.read().strip()

    if content:
        return content
    else:
        return None
    

def clean():
    file_path = "talk.txt"

    with open(file_path, "w") as file:
        file.truncate(0)


if __name__ == '__main__':
    listen()