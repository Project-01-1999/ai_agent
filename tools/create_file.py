from pathlib import Path
from tools.base_tool import BaseTool


class CreateFileTool:
    
    @property
    def name(self):
        return "create_file"

    def run(self, file_path: str):

        path = Path(file_path)

        try:
            # Create parent folders if they don't exist
            path.parent.mkdir(parents=True, exist_ok=True)

            # Check if file already exists
            if path.exists():
                return f"File already exists: {file_path}"

            # Create an empty file
            path.touch()

            return f"File created successfully: {file_path}"

        except Exception as e:
            return f"Error creating file: {e}"