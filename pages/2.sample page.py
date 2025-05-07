#this is sample page

import streamlit as st
import pandas as pd
import os
from io import BytesIO

def clear_text(): # this is the function you define (def is a Python keyword and is short for 'define')
  st.session_state["TextBox"]=''
  st.session_state["2"] = ''  # add "text" as a key using the square brackets notation and set it to have the value '' 

#Set up our app
st.set_page_config(page_title="💽 Data Sweeper",layout="wide")

st.write ( "Sample testing")

#st.write("Button not Pressed")
x=st.text_input("Favourite color",key="TextBox")
st.write(f"your Favorite color is:{x}")
V_Textbox=st.text_input("No.of Text boxes")


#st.button({x})

b=st.button("Click me")
if b:
    st.write("Button Pressed")
    st.write(f"Your colour is: {x}")
    st.write("You did it")
    

st.text_area("Text Area Nilesh",key=2)
#vTextareaRequest = st.text_area("Request", key="request_text")
#Nilesh code

st.write("### Input Data")
col1,col2,col3 = st.columns(3)

#VTextBoxesCount= col1.number_input("Text box", min_value=0, value=500)
#VCheckBoxesCount = col1.number_input("CheckBox", min_value=0, value=10)
#VListBoxCount = col1.number_input("Listbox", min_value=0, value=10)
#VRadioBoxCount = col2.number_input("RadioButton", min_value=0, value=3)
#VButtonCount_OK= col2.number_input("OK Button", min_value=0, value=1)
#VButtonCount_Cancel = col2.number_input("Cancel Button", min_value=0, value=1)

VTextBoxesCount= col1.text_input("Text box")
VCheckBoxesCount = col1.text_input("CheckBox")
VListBoxCount = col1.text_input("Listbox")
VRadioBoxCount = col2.text_input("RadioButton")
VButtonCount_OK= col2.text_input("OK Button")
VButtonCount_Cancel = col2.text_input("Cancel Button")


VTextBoxesCountStr= col1.text_input("Text box2")

#concatenated_text="Write Testcase for "+ VTextBoxesCount+" TextBoxes, "+VCheckBoxesCount+" Check boxes,"
concatenated_text="Write Testcase for "+ VTextBoxesCount+" TextBoxes, "+VCheckBoxesCount+" Check boxes,"+ VListBoxCount +" List Boxes," +VRadioBoxCount+" Radio Buttons,"+ VButtonCount_OK +" OK Button," + VButtonCount_Cancel+" Cancel Button"

st.write(concatenated_text)

b=st.button("Generate Test case")
if b:
    st.write ("Button Pressed")
    st.button
else :
    st.write("not Pressed")


def disable(b):
    st.session_state["disabled"] = b

button_a = st.button('a', key='but_a', on_click=disable, args=(False,))
button_b = st.button('b', key='but_b', on_click=disable, args=(True,))
button_c = st.button('c', key='but_c', disabled=st.session_state.get("disabled", False))
button_d = st.button('d', key='but_d', on_click=disable, args=(False,))


st.button("Clear text", on_click=clear_text)


if button_d:
   
    st.write("Button C Pressed")
    
   #button_c=st.session_state.get("disabled", True)