import os
from settings import PROJECTS_FOLDER


class Executor:

    def __init__(self, registry):
        self.registry = registry

    def execute(self, plan):
        
        results = []

        for step in plan:

            tool_name = step["tool"]
            args = step["args"]

            tool = self.registry.get_tool(tool_name)

            if tool is None:
                results.append(f"Tool not found: {tool_name}")
                continue

            full_args = []

            for arg in args:
                full_args.append(os.path.join(PROJECTS_FOLDER, arg))

            result = tool.run(*full_args)

            results.append(result)
            
        return "\n".join(results)