from langchain_core.prompts import ChatPromptTemplate

writing_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Writing Agent.

Rules:
- Write professional documentation.
- Write reports.
- Write README files.
- Write explanations.
- Do not generate code.
"""
        ),
        ("human", "{task}")
    ]
)