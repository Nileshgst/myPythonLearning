import streamlit as st
from typing import Generator
from groq import Groq

st.set_page_config(page_icon="💬", layout="wide",
                   page_title="Chatbot using Groq ...")

def clear_text(): # this is the function you define (def is a Python keyword and is short for 'define')
    st.session_state["Textbox1"] = ''  # add "text" as a key using the square brackets notation and set it to have the value '' 
    st.session_state["Textbox2"] = '' 
    st.session_state["Textbox3"] = '' 
    st.session_state["Textbox4"] = '' 
    st.session_state["Textbox5"] = '' 
    st.session_state["Textbox6"] = '' 
st.session_state.messages = []
st.session_state.messages2 = [] 

def display_heading(heading_text):
  """Displays the given text as a heading Testing Nilesh."""
  print("=" * len(heading_text))
  print(heading_text)
  print("=" * len(heading_text))



def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


icon("💽")
# Example usage:
#display_heading("Nilesh's Page")

#st.subheader("Nilesh's Groq Chat Streamlit App Testing", divider="rainbow", anchor=False)
st.subheader("Nilesh's Chatbot for Functional Testing", divider="blue",anchor=False)
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)

# Initialize chat history and selected model
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None

# Define model details
models = {
    "gemma2-9b-it": {"name": "Gemma2-9b-it", "tokens": 8192, "developer": "Google"},
    "llama-3.3-70b-versatile": {"name": "LLaMA3.3-70b-versatile", "tokens": 128000, "developer": "Meta"},
    "llama-3.1-8b-instant" : {"name": "LLaMA3.1-8b-instant", "tokens": 128000, "developer": "Meta"},
    "llama3-70b-8192": {"name": "LLaMA3-70b-8192", "tokens": 8192, "developer": "Meta"},
    "llama3-8b-8192": {"name": "LLaMA3-8b-8192", "tokens": 8192, "developer": "Meta"},
    "mixtral-8x7b-32768": {"name": "Mixtral-8x7b-Instruct-v0.1", "tokens": 32768, "developer": "Mistral"},
}

# Layout for model selection and max_tokens slider
col1, col2 = st.columns(2)

with col1:
    model_option = st.selectbox(
        "Choose a model:",
        options=list(models.keys()),
        format_func=lambda x: models[x]["name"],
        index=4  # Default to mixtral
    )

# Detect model change and clear chat history if model has changed
if st.session_state.selected_model != model_option:
    st.session_state.messages = []
    st.session_state.messages2 = []
    st.session_state.selected_model = model_option

max_tokens_range = models[model_option]["tokens"]

with col2:
    # Adjust max_tokens slider dynamically based on the selected model
    max_tokens = st.slider(
        "Max Tokens:",
        min_value=512,  # Minimum value to allow some flexibility
        max_value=max_tokens_range,
        # Default value or max allowed if less
        value=min(32768, max_tokens_range),
        step=512,
        help=f"Adjust the maximum number of tokens (words) for the model's response. Max for selected model: {max_tokens_range}"
    )

#Nilesh code
#st.write("### Input Data")
st.subheader("Input Data", anchor=False)
#vApiPrompt ="Write Test cases in a table format for API Testing for the following Sample Request and Resposne \n"

# concatenated_text="Write Testcase for "+ VTextBoxesCount+" TextBoxes, "+VCheckBoxesCount+" Check boxes,"+ VListBoxCount +" List Boxes," +VRadioBoxCount+" Radio Buttons,"+ VButtonCount_OK +" OK Button," + VButtonCount_Cancel+" Cancel Button"

# st.write(concatenated_text)
if "request_text" not in st.session_state:
    st.session_state["request_text"] = ""
if "response_text" not in st.session_state:
    st.session_state["response_text"] = ""


#Nilesh code

#st.write("### Input Data Functional Testing")
col1,col2,col3,col4,col5 = st.columns(5)
VTextBoxesCount= col1.text_input("Text box", max_chars=2,key="Textbox1")
VCheckBoxesCount = col2.text_input("CheckBox",max_chars=1,key="Textbox2")
VListBoxCount = col3.text_input("Listbox",max_chars=1,key="Textbox3")
VRadioBoxCount = col4.text_input("RadioButton",max_chars=1,key="Textbox4")
VButtonCount_OK= col1.text_input("OK Button",max_chars=1,key="Textbox5")
VButtonCount_Cancel = col2.text_input("Cancel Button",max_chars=1,key="Textbox6")



# VTextBoxesCountStr= col1.text_input("Text box2")
#VTextBoxesCount = col1.number_input("Text box", min_value=0, value=50,key="Textbox" )
#VTextBoxesCount=str(VTextBoxesCount)
#VTextBoxesCount = col1.number_input("Text box",key="Textbox" )
#VTextBoxesCount= col1.number_input("Text box", key= "Textbox2")
# VRadioBoxCount = str(col4.number_input("RadioButton",min_value=0,max_value=5))
#VListBoxCount = col1.text_input("Listbox")
#VRadioBoxCount = col2.text_input("RadioButton")
# VButtonCount_OK= str(col1.number_input("OK Button",min_value=0,max_value=5))
# VButtonCount_Cancel = str(col2.number_input("Cancel Button",min_value=0,max_value=5))
#VTextBoxesCountStr= col1.text_input("Text box2")

#concatenated_text="Write Testcase for "+ VTextBoxesCount+" TextBoxes, "+VCheckBoxesCount+" Check boxes,"
concatenated_text_manual="Write Manual Testcase for "+ VTextBoxesCount+" TextBoxes, "+VCheckBoxesCount+" Check boxes,"+ VListBoxCount +" List Boxes," +VRadioBoxCount+" Radio Buttons,"+ VButtonCount_OK +" OK Button," + VButtonCount_Cancel+" Cancel Button"
concatenated_text_selenium="Write Selenium Automation script for "+ VTextBoxesCount+" TextBoxes, "+VCheckBoxesCount+" Check boxes,"+ VListBoxCount +" List Boxes," +VRadioBoxCount+" Radio Buttons,"+ VButtonCount_OK +" OK Button," + VButtonCount_Cancel+" Cancel Button"
st.write("contacted text is" +concatenated_text_manual)

#End Nilesh Code

# vTextareaRequest = st.text_area("Request", key="request_text")
# vTextareaResponse = st.text_area("Response", key="response_text")
# vTextareaRequest= "\n Request is \n"+vTextareaRequest+"\n"
# vTextareaResponse="\n Response is \n"+vTextareaResponse+"\n"
# vApiPrompt=vApiPrompt+  vTextareaRequest +vTextareaResponse
# st.write(vApiPrompt)


# col1,col2,col3 = st.columns(3)
# #VTextBoxesCount= col1.text_input("Text box")
# VTextBoxesCount = col1.number_input("Text box", min_value=0, value=50)
# VTextBoxesCount=str(VTextBoxesCount)
# #VTextBoxesCount= col1.text_input("Text box")
# VCheckBoxesCount = str(col1.number_input("CheckBox",min_value=0, value=5))



#concatenated_text="Write Testcase for "+ VTextBoxesCount+" TextBoxes, "+VCheckBoxesCount+" Check boxes,"
#concatenated_text="Write Testcase for "+ VTextBoxesCount+" TextBoxes, "+VCheckBoxesCount+" Check boxes,"+ VListBoxCount +" List Boxes," +VRadioBoxCount+" Radio Buttons,"+ VButtonCount_OK +" OK Button," + VButtonCount_Cancel+" Cancel Button"

#st.write(concatenated_text)
#End Nilesh Code

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    avatar = '🤖' if message["role"] == "assistant" else '👨‍💻'
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
    """Yield chat response content from the Groq API response."""
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

#To clear text area
# st.button("Clear text", on_click=clear_text)

#if prompt := st.chat_input("Enter your prompt here..."):

col1, col2,col3 =st.columns(3)
with col1:
    b=st.button("Generate Test case")
with col2:
    d=st.button("Selenium Automation Test cases")

with col3:
    c=st.button("Clear Session", on_click=clear_text)


if prompt := b :

    #rompt2 = "Context: "+"\nQuery: "+prompt+"\nTask: Answer Query in Detail"
    # prompt2 = "Context: "+"\nQuery: "+"\nTask: Answer Query in Detail"
    #added by Nilesh
    #prompt2 = "Context: "+"\nQuery: "+concatenated_text+"\nTask: Answer Query in Detail"
    prompt2 = "Context: "+"\nQuery: "+concatenated_text_manual+"\nTask: Answer Query in Detail"
    prompt2 = "Query: "+concatenated_text_manual+" Task: Answer Query with sufficient examples and in Detail"
    st.write(prompt2)
    #end added by Nilesh
    st.session_state.messages2.append({"role": "user", "content": prompt2})

    with st.chat_message("user", avatar='👨‍💻'):
             st.markdown(prompt)
           #st.markdown(concatenated_text)
    # Fetch response from Groq API
    try:
        chat_completion = client.chat.completions.create(
            model=model_option,
            messages=[
                {
                    "role": m["role"],
                    "content": m["content"]
                }
                for m in st.session_state.messages2
            ],
            max_tokens=max_tokens,
            stream=True
        )

        # Use the generator function with st.write_stream
        with st.chat_message("assistant", avatar="🤖"):
            chat_responses_generator = generate_chat_responses(chat_completion)
            full_response = st.write_stream(chat_responses_generator)
    except Exception as e:
        st.error(e, icon="🚨")

    # Append the full response to session_state.messages
    if isinstance(full_response, str):
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response})
        st.session_state.messages2.append(
            {"role": "assistant", "content": full_response})
    else:
        # Handle the case where full_response is not a string
        combined_response = "\n".join(str(item) for item in full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": combined_response})
        st.session_state.messages2.append(
            {"role": "assistant", "content": combined_response})



if prompt:=d:
    prompt2 = "Context: "+"\nQuery: "+"\nTask: Answer Query in Detail"
    #added by Nilesh
    #prompt2 = "Context: "+"\nQuery: "+concatenated_text+"\nTask: Answer Query in Detail"
    prompt2 = "Context: "+"\nQuery: "+concatenated_text_selenium+"\nTask: Answer Query in Detail"
    st.write(prompt2)
    #end added by Nilesh
    st.session_state.messages2.append({"role": "user", "content": prompt2})


# if prompt:=c:
#    #if st.session_state.selected_model != model_option:
#     sxt.session_state.messages = []
#     st.session_state.messages2 = []
    #st.session_state.selected_model = model_option 

#st.session_state.messages.append({"role": "user", "content": prompt})



    with st.chat_message("user", avatar='👨‍💻'):
             st.markdown(prompt)
           #st.markdown(concatenated_text)
    # Fetch response from Groq API
    try:
        chat_completion = client.chat.completions.create(
            model=model_option,
            messages=[
                {
                    "role": m["role"],
                    "content": m["content"]
                }
                for m in st.session_state.messages2
            ],
            max_tokens=max_tokens,
            stream=True
        )

        # Use the generator function with st.write_stream
        with st.chat_message("assistant", avatar="🤖"):
            chat_responses_generator = generate_chat_responses(chat_completion)
            full_response = st.write_stream(chat_responses_generator)
    except Exception as e:
        st.error(e, icon="🚨")

    # Append the full response to session_state.messages
    if isinstance(full_response, str):
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response})
        st.session_state.messages2.append(
            {"role": "assistant", "content": full_response})
    else:
        # Handle the case where full_response is not a string
        combined_response = "\n".join(str(item) for item in full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": combined_response})
        st.session_state.messages2.append(
            {"role": "assistant", "content": combined_response})

