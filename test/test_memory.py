from planner import PlannerAgent

from router import Router

planner = PlannerAgent()

router = Router()

todos = planner.create_plan(
    "Build an Online Shopping Website"
)

router.execute(todos)

print("Completed")