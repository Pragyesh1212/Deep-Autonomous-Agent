from planner import PlannerAgent
from router import Router
from combiner import Combiner

planner = PlannerAgent()
router = Router()
combiner = Combiner()

user_request = "Build an Online Shopping Website"

todos = planner.create_plan(user_request)

router.execute(todos)

final_answer = combiner.combine(user_request)

print("\n")
print("=" * 50)
print(final_answer)