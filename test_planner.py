from planner import Planner

planner = Planner()

plan = planner.create_project_plan("WeatherApp")

for step in plan:
    print(step)