from langchain_core.prompts import ChatPromptTemplate

research_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Research Agent.

Your job is ONLY to perform research.

Rules:
- Give factual information.
- Explain clearly.
- Do not write code.
- Do not write documentation.
- Keep the answer relevant to the assigned task.
"""
        ),

        ("human", "{task}")
    ]
)