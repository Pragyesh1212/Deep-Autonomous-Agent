import streamlit as st


# -------------------------------------------------------
# Get Current Chat
# -------------------------------------------------------

def get_current_chat():

    chat_id = st.session_state.current_chat

    return st.session_state.chats[chat_id]


# -------------------------------------------------------
# Show Chat Messages
# -------------------------------------------------------

def show_chat():

    chat = get_current_chat()

    for message in chat["messages"]:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])


# -------------------------------------------------------
# Add User Message
# -------------------------------------------------------

def add_user_message(text):

    chat = get_current_chat()

    chat["messages"].append(

        {

            "role": "user",

            "content": text

        }

    )


# -------------------------------------------------------
# Add Assistant Message
# -------------------------------------------------------

def add_ai_message(text):

    chat = get_current_chat()

    chat["messages"].append(

        {

            "role": "assistant",

            "content": text

        }

    )


# -------------------------------------------------------
# Get Current Result
# -------------------------------------------------------

def get_result():

    chat = get_current_chat()

    return chat["result"]


# -------------------------------------------------------
# Set Current Result
# -------------------------------------------------------

def set_result(result):

    chat = get_current_chat()

    chat["result"] = result