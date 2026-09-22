from planner import PlannerAgent
from router import Router
from combiner import Combiner
from quality_checker import QualityChecker

planner = PlannerAgent()
router = Router()
combiner = Combiner()
quality = QualityChecker()

user_request = "Build an Online Shopping Website"

todos = planner.create_plan(user_request)

router.execute(todos)

combined = combiner.combine(user_request)

result = quality.check(combined)

print()

print("=" * 60)

print("QUALITY SCORE")

print(result["score"])

print()

print("=" * 60)

print("FINAL OUTPUT")

print(result["output"])