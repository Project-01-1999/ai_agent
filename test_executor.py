from planner import Planner
from tool_registry import ToolRegistry
from executor import Executor

planner = Planner()
registry = ToolRegistry()
executor = Executor(registry)

plan = planner.create_project_plan("WeatherApp")

executor.execute(plan)