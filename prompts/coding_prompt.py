from langchain_core.prompts import ChatPromptTemplate

coding_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Coding Agent.

Rules:
- Write clean Python code.
- Explain only if necessary.
- Focus only on coding.
- Do not do research.
- Do not write documentation.
"""
        ),
        ("human", "{task}")
    ]
)