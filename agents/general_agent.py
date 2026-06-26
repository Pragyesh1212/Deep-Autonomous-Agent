from utils.llm import llm
from prompts.general_prompt import general_prompt


class GeneralAgent:

    def run(self, task):

        chain = general_prompt | llm

        response = chain.invoke(
            {
                "task": task
            }
        )

        return response.content