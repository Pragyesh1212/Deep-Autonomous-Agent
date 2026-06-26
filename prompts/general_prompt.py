from langchain_core.prompts import ChatPromptTemplate

general_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a General Assistant.

Answer the assigned task clearly and concisely.
"""
        ),
        ("human", "{task}")
    ]
)