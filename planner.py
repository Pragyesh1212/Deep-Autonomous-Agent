from prompts.planner_prompt import planner_prompt
from utils.llm import llm


class PlannerAgent:

    def create_plan(self, user_input):

        chain = planner_prompt | llm

        response = chain.invoke(
            {
                "input": user_input
            }
        )

        lines = response.content.split("\n")

        todos = []

        current_task = ""

        task_id = 1

        for line in lines:

            line = line.strip()

            if line.startswith("Task:"):

                current_task = line.replace("Task:", "").strip()

            elif line.startswith("Agent:"):

                agent = line.replace("Agent:", "").strip().lower()

                todos.append(
                    {
                        "id": task_id,
                        "task": current_task,
                        "agent": agent,
                        "status": "Pending"
                    }
                )

                task_id += 1

        return todos