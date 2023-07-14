

import streamlit as st
import pandas as pd
import numpy as np

if 'my_value' not in st.session_state:
    st.session_state['my_value'] = 0
    
def get_data():
    print("get_data .... 1111")
    
get_data()   

def btn_click():
    print("aaaa")
    st.session_state['my_value'] =  st.session_state['my_value'] + 1 
    st.write('Goodbye 111') 

animal = st.text_input('Type an animal') 

if st.button('Say hello',on_click=btn_click): 
    st.write('Why hello there')
    print("aaaa11")
else:
    st.write('Goodbye')
    print("aaaa22")

st.title('aa bb cc' + str(st.session_state['my_value'])) 

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

print("tab1————",tab1,"tab2", tab2, "tab3", tab3)

with tab1:
    print("11111")
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    print("22222")
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    print("33333")
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   
with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))
   