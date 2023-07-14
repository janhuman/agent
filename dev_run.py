import lbai_agent.main_interface
import lbai_agent.openai_langchain as lc
from langchain.chat_models import ChatOpenAI
from lbai_agent.intention_judge import read_list, judge
from redis_utils import pub_sub

def test1():
    lbai_agent.main_interface.main()
    #read_list()
    
    #judge('请你对usr目录下的每一个文件都加上‘-1’')
    #print(lc.base_chat("你好"))
    #pub_sub.publish_message("1", "你好")




if __name__ == '__main__':
    test1()