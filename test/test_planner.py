from planner import PlannerAgent

planner = PlannerAgent()

todos = planner.create_plan(
    "Build an Online Shopping Website"
)

print()

for todo in todos:

    print(todo)