from utils.llm import llm
from prompts.writing_prompt import writing_prompt


class WritingAgent:

    def run(self, task):

        chain = writing_prompt | llm

        response = chain.invoke(
            {
                "task": task
            }
        )

        return response.content