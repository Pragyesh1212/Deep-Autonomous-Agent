from utils.llm import llm
from prompts.research_prompt import research_prompt


class ResearchAgent:

    def run(self, task):

        chain = research_prompt | llm

        response = chain.invoke(
            {
                "task": task
            }
        )

        return response.content