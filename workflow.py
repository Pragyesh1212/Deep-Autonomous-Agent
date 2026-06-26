from langgraph.graph import StateGraph, START, END

from state import AgentState

from planner import PlannerAgent
from router import Router
from combiner import Combiner
from quality_checker import QualityChecker

from tools.memory_tool import MemoryTool


# ==========================================================
# Initialize Components
# ==========================================================

planner = PlannerAgent()
router = Router()
combiner = Combiner()
quality_checker = QualityChecker()
memory = MemoryTool()


# ==========================================================
# Planner Node
# ==========================================================

def planner_node(state: AgentState):

    print("\n========== Planner ==========")

    # Clear memory only for the current chat
    memory.clear(state["thread_id"])

    todos = planner.create_plan(
        state["user_input"]
    )

    state["todos"] = todos

    return state


# ==========================================================
# Router Node
# ==========================================================

def router_node(state: AgentState):

    print("\n========== Router ==========")

    outputs = router.execute(

        state["todos"],

        state["thread_id"]

    )

    state["agent_outputs"] = outputs

    # ----------------------------------------
    # Store Agent Quality
    # ----------------------------------------

    quality = {}

    for task_id, data in outputs.items():

        quality[task_id] = {

            "agent": data["agent"],

            "score": data["quality_score"],

            "feedback": data["feedback"]

        }

    state["agent_quality"] = quality

    return state


# ==========================================================
# Combiner Node
# ==========================================================

def combiner_node(state: AgentState):

    print("\n========== Combiner ==========")

    combined = combiner.combine(

        state["user_input"],

        state["thread_id"]

    )

    state["combined_output"] = combined

    return state
# ==========================================================
# Final Quality Checker
# ==========================================================

def quality_node(state: AgentState):

    print("\n========== Final Quality Checker ==========")

    result = quality_checker.check(

        agent="final",

        user_input=state["user_input"],

        output=state["combined_output"]

    )

    state["quality_score"] = result["score"]

    state["feedback"] = result["feedback"]

    state["final_output"] = result["output"]

    return state


# ==========================================================
# Build LangGraph
# ==========================================================

builder = StateGraph(AgentState)

builder.add_node("Planner", planner_node)

builder.add_node("Router", router_node)

builder.add_node("Combiner", combiner_node)

builder.add_node("Quality", quality_node)

builder.add_edge(START, "Planner")

builder.add_edge("Planner", "Router")

builder.add_edge("Router", "Combiner")

builder.add_edge("Combiner", "Quality")

builder.add_edge("Quality", END)

graph = builder.compile()


# ==========================================================
# Run Workflow
# ==========================================================

def run_workflow(user_input, thread_id):

    initial_state = {

        "user_input": user_input,

        "thread_id": thread_id,

        "todos": [],

        "current_task": {},

        "virtual_files": {},

        "agent_outputs": {},

        "agent_quality": {},

        "combined_output": "",

        "quality_score": 0,

        "feedback": [],

        "final_output": ""

    }

    result = graph.invoke(initial_state)

    return result
# ==========================================================
# Run from Terminal
# ==========================================================

if __name__ == "__main__":

    user_prompt = input("Enter your task: ")

    # Default thread for terminal execution
    result = run_workflow(
        user_prompt,
        "terminal_chat"
    )

    print("\n")
    print("=" * 80)
    print("AGENT QUALITY REPORT")
    print("=" * 80)

    if result.get("agent_quality"):

        for task_id, info in result["agent_quality"].items():

            print(f"\nTask {task_id}")

            print(f"Agent : {info['agent']}")

            print(f"Score : {info['score']}/100")

            print("Feedback:")

            for item in info["feedback"]:

                print(f"  • {item}")

    else:

        print("No agent quality information available.")

    print("\n")
    print("=" * 80)
    print("FINAL QUALITY")
    print("=" * 80)

    print(f"Score : {result['quality_score']}/100")

    print("\nFeedback:")

    for item in result["feedback"]:

        print(f"• {item}")

    print("\n")
    print("=" * 80)
    print("FINAL RESPONSE")
    print("=" * 80)

    print(result["final_output"])