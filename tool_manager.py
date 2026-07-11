from tools.create_folder import CreateFolderTool


class ToolManager:

    def __init__(self):
        self.folder_tool = CreateFolderTool()

    def create_folder(self, folder_path):
        return self.folder_tool.run(folder_path)