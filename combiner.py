from tools.memory_tool import MemoryTool
from prompts.combiner_prompt import combiner_prompt
from utils.llm import llm


class Combiner:

    def __init__(self):

        self.memory = MemoryTool()

    def combine(self, user_request, thread_id):

        outputs = self.memory.read_all(thread_id)

        context = f"""
Original User Request:

{user_request}

----------------------------------------

Task Outputs

"""

        for item in outputs:

            context += f"""

==========================

Source File : {item["file"]}

Output:

{item["content"]}

"""

        chain = combiner_prompt | llm

        response = chain.invoke(

            {

                "content": context

            }

        )

        return response.content