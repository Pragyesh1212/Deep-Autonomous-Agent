from agents.research_agent import ResearchAgent
from agents.coding_agent import CodingAgent
from agents.writing_agent import WritingAgent
from agents.analysis_agent import AnalysisAgent
from agents.general_agent import GeneralAgent

from tools.memory_tool import MemoryTool
from quality_checker import QualityChecker


class Router:

    def __init__(self):

        self.memory = MemoryTool()

        self.quality = QualityChecker()

        self.research = ResearchAgent()
        self.coding = CodingAgent()
        self.writing = WritingAgent()
        self.analysis = AnalysisAgent()
        self.general = GeneralAgent()

    # -------------------------------------------------
    # Execute Planned Tasks
    # -------------------------------------------------

    def execute(self, todos, thread_id):

        outputs = {}

        for todo in todos:

            task = todo["task"]
            agent = todo["agent"]

            print("\n" + "=" * 60)
            print(f"Executing Task {todo['id']}")
            print(f"Task   : {task}")
            print(f"Agent  : {agent}")

            todo["status"] = "Running"

            # ---------------------------------------
            # Execute Correct Agent
            # ---------------------------------------

            if agent == "research":

                result = self.research.run(task)

            elif agent == "coding":

                result = self.coding.run(task)

            elif agent == "writing":

                result = self.writing.run(task)

            elif agent == "analysis":

                result = self.analysis.run(task)

            else:

                result = self.general.run(task)

            # ---------------------------------------
            # Quality Check
            # ---------------------------------------

            quality = self.quality.check(

                agent=agent,

                user_input=task,

                output=result

            )

            # ---------------------------------------
            # Save Output in Current Chat Memory
            # ---------------------------------------

            self.memory.write(

                thread_id,

                todo["id"],

                quality["output"]

            )

            todo["status"] = "Completed"

            outputs[todo["id"]] = {

                "task": task,

                "agent": agent,

                "status": todo["status"],

                "quality_score": quality["score"],

                "feedback": quality["feedback"],

                "output": quality["output"]

            }

            print(f"Quality Score : {quality['score']}")

            print("Feedback:")

            for item in quality["feedback"]:

                print("-", item)

            print(f"Task {todo['id']} Completed")

        return outputs