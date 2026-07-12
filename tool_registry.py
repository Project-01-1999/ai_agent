import pkgutil
import importlib
import inspect

from tools.base_tool import BaseTool


class ToolRegistry:

    def __init__(self):
        self.tools = {}
        self.load_tools()

    def load_tools(self):

        import tools

        for _, module_name, _ in pkgutil.iter_modules(tools.__path__):

            if module_name == "base_tool":
                continue

            module = importlib.import_module(f"tools.{module_name}")

            for _, obj in inspect.getmembers(module, inspect.isclass):

                if issubclass(obj, BaseTool) and obj is not BaseTool:

                    tool = obj()

                    self.tools[tool.name] = tool

    def get_tool(self, name):

        return self.tools.get(name)

    def list_tools(self):

        return list(self.tools.keys())