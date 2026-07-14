from json import tool

from llm import LLM
from tool_registry import ToolRegistry
from planner import Planner
from executor import Executor
from settings import PROJECTS_FOLDER
from intent_parser import IntentParser

import os


class AstraController:

    def __init__(self):
        self.llm = LLM()
        self.registry = ToolRegistry()
        self.planner = Planner()
        self.executor = Executor(self.registry)
        self.parser = IntentParser()

    def chat(self, user_message):

            intent = self.parser.parse(user_message)

            if intent["intent"] == "create_folder":

                folder_path = os.path.join(
                PROJECTS_FOLDER,
                intent["name"]
                )

                tool = self.registry.get_tool("create_folder")
                return tool.run(folder_path)

            elif intent["intent"] == "create_file":

                file_path = os.path.join(
                PROJECTS_FOLDER,
                intent["name"]
                )

                tool = self.registry.get_tool("create_file")
                return tool.run(file_path)
            
            elif intent["intent"] == "create_python_project":

                plan = self.planner.create_python_project_plan(
                intent["name"]
                )

                return self.executor.execute(plan)
            return self.llm.ask(user_message)
            

