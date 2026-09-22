from utils.llm import llm
from prompts.coding_prompt import coding_prompt


class CodingAgent:

    def run(self, task):

        chain = coding_prompt | llm

        response = chain.invoke(
            {
                "task": task
            }
        )

        return response.content