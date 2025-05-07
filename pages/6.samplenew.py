import streamlit as st
st.write("Hello Nilesh")

#def main():
def clear_text(): # this is the function you define (def is a Python keyword and is short for 'define')
  st.session_state["1"] = ''  # add "text" as a key using the square brackets notation and set it to have the value '' 

# st.help(st.text_area)
st.title("Streamlite app")
st.subheader("Hello team")
with st.form(key="myform",clear_on_submit=True):
         firstname = st.text_input("FirstName")
         message = st.text_area("Message",key=1)
         submit_button=st.form_submit_button("Submit")

#To clear text area
st.button("Clear text", on_click=clear_text)
st.write (1) 

# if submit_button:
#          st.info("Results")
#          results=firstname+message
#          st.write(results)