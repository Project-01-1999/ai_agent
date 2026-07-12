from llm import LLM
from tool_manager import ToolManager
from settings import PROJECTS_FOLDER
from intent_parser import IntentParser
import os


class AstraController:

    def __init__(self):
        self.llm = LLM()
        self.tools = ToolManager()
        self.parser = IntentParser()

    def chat(self, user_message):

            intent = self.parser.parse(user_message)

            if intent["intent"] == "create_folder":

                folder_path = os.path.join(
                PROJECTS_FOLDER,
                intent["name"]
                )

                return self.tools.create_folder(folder_path)

            elif intent["intent"] == "create_file":

                file_path = os.path.join(
                PROJECTS_FOLDER,
                intent["name"]
                )

                return self.tools.create_file(file_path)

            else:

                return self.llm.ask(user_message)
