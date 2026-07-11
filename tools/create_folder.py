from pathlib import Path


class CreateFolderTool:

    def run(self, folder_path: str):

        path = Path(folder_path)

        if path.exists():
            return f"Folder already exists: {folder_path}"

        path.mkdir(parents=True)

        return f"Folder created successfully: {folder_path}"