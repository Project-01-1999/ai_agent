from llm import LLM
from tool_manager import ToolManager
from settings import PROJECTS_FOLDER
import os


class AstraController:

    def __init__(self):
        self.llm = LLM()
        self.tools = ToolManager()

    def chat(self, user_message):

        message = user_message.lower().strip()

        # Folder creation intent
        if message.startswith("create folder "):

            folder_name = user_message[len("create folder "):].strip()

            folder_path = os.path.join(PROJECTS_FOLDER, folder_name)

            return self.tools.create_folder(folder_path)

        # Default: ask the LLM
        return self.llm.ask(user_message)