import uuid
import streamlit as st

from workflow import run_workflow

from ui.sidebar import show_sidebar

from ui.chat import (
    show_chat,
    add_user_message,
    add_ai_message,
    get_result,
    set_result
)

# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(

    page_title="Deep Autonomous Agent",

    page_icon="🤖",

    layout="wide"

)

st.title("Deep Autonomous Agent")

# ----------------------------------------------------
# Initialize Chats
# ----------------------------------------------------

if "chats" not in st.session_state:

    first_chat = str(uuid.uuid4())

    st.session_state.chats = {

        first_chat: {

            "title": "New Chat",

            "messages": [],

            "thread_id": first_chat,

            "result": None

        }

    }

    st.session_state.current_chat = first_chat

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

show_sidebar(
    get_result()
)

# ----------------------------------------------------
# Chat Window
# ----------------------------------------------------

show_chat()

# ----------------------------------------------------
# Chat Input
# ----------------------------------------------------

prompt = st.chat_input(
    "Enter your task..."
)

if prompt:

    add_user_message(prompt)

    current_chat = st.session_state.current_chat

    thread_id = st.session_state.chats[
        current_chat
    ]["thread_id"]

    with st.spinner(
        "Executing Autonomous Workflow..."
    ):

        result = run_workflow(

            prompt,

            thread_id

        )
        
        set_result(result)

    add_ai_message(
        result["final_output"]
    )

    # -----------------------------------------
    # Auto Chat Title
    # -----------------------------------------

    current_title = st.session_state.chats[current_chat]["title"]

    # Rename the chat only the first time
    if current_title == "New Chat" or current_title.startswith("Chat"):

        title = prompt.strip()

        # Remove line breaks
        title = title.replace("\n", " ")

        # Keep title length reasonable
        if len(title) > 35:
            title = title[:35] + "..."

        st.session_state.chats[current_chat]["title"] = title

    st.rerun()
