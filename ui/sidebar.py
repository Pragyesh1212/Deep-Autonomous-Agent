import uuid
import streamlit as st


def create_new_chat():

    chat_id = str(uuid.uuid4())

    chat_number = len(st.session_state.chats) + 1

    st.session_state.chats[chat_id] = {

        "title": f"Chat {chat_number}",

        "messages": [],

        "thread_id": chat_id,

        "result": None

    }

    st.session_state.current_chat = chat_id

    st.rerun()


def show_sidebar(result=None):

    with st.sidebar:

        st.title("Deep Autonomous Agent")

        # -------------------------------------
        # New Chat
        # -------------------------------------

        if st.button("➕ New Chat", use_container_width=True):

            create_new_chat()

        st.divider()

        # -------------------------------------
        # Chat History
        # -------------------------------------

        st.subheader("💬 Chat History")

        for chat_id, chat in st.session_state.chats.items():

            if st.button(

                chat["title"],

                key=chat_id,

                use_container_width=True

            ):

                st.session_state.current_chat = chat_id

                st.rerun()

        st.divider()

        # -------------------------------------
        # Current Chat Result
        # -------------------------------------

        current_chat = st.session_state.current_chat

        result = st.session_state.chats[current_chat]["result"]

        # -------------------------------------
        # Tasks
        # -------------------------------------

        st.subheader("📋 Tasks")

        if result:

            for todo in result["todos"]:

                if todo["status"] == "Completed":

                    icon = "✅"

                elif todo["status"] == "Running":

                    icon = "🔄"

                else:

                    icon = "⏳"

                st.write(f"{icon} {todo['task']}")

        else:

            st.info("No tasks yet.")

        st.divider()

        # -------------------------------------
        # Agent Quality
        # -------------------------------------

        st.subheader("🤖 Agent Quality")

        if result:

            for _, info in result["agent_quality"].items():

                if info["score"] >= 90:

                    emoji = "🟢"

                elif info["score"] >= 75:

                    emoji = "🟡"

                else:

                    emoji = "🔴"

                st.write(

                    f"{emoji} **{info['agent'].title()}** : {info['score']}/100"

                )

        else:

            st.write("No quality information.")

        st.divider()

        # -------------------------------------
        # Final Quality
        # -------------------------------------

        st.subheader("⭐ Final Quality")

        if result:

            st.metric(

                "Overall Score",

                f"{result['quality_score']}/100"

            )

        else:

            st.metric(

                "Overall Score",

                "--"

            )

        st.divider()

        # -------------------------------------
        # Feedback
        # -------------------------------------

        st.subheader("💬 Feedback")

        if result:

            for item in result["feedback"]:

                st.write(f"• {item}")

        else:

            st.write("No feedback.")

        st.divider()

        # -------------------------------------
        # Virtual Memory
        # -------------------------------------

        st.subheader("💾 Virtual Memory")

        if result:

            for todo in result["todos"]:

                st.write(f"📄 task_{todo['id']}.txt")

        else:

            st.write("No memory files.")
