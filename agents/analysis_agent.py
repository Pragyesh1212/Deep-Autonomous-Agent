from utils.llm import llm
from prompts.analysis_prompt import analysis_prompt


class AnalysisAgent:

    def run(self, task):

        chain = analysis_prompt | llm

        response = chain.invoke(
            {
                "task": task
            }
        )

        return response.content