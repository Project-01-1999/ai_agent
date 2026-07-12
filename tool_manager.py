from tools.create_folder import CreateFolderTool
from tools.create_file import CreateFileTool


class ToolManager:

    def __init__(self):
        self.folder_tool = CreateFolderTool()
        self.file_tool = CreateFileTool()

    def create_folder(self, folder_path):
        return self.folder_tool.run(folder_path)

    def create_file(self, file_path):
        return self.file_tool.run(file_path)