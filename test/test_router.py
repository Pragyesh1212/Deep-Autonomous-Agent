from planner import PlannerAgent

from router import Router


planner = PlannerAgent()

router = Router()


todos = planner.create_plan(
    "Build an Online Shopping Website"
)


outputs = router.execute(todos)


print("\n")

print(outputs)