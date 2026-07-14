from pathlib import Path
from tools.base_tool import BaseTool


class CreateFileTool(BaseTool):

    @property
    def name(self):
        return "create_file"

    def run(self, file_path: str):

        path = Path(file_path)

        try:
            path.parent.mkdir(parents=True, exist_ok=True)

            if path.exists():
                return f"File already exists: {file_path}"

            path.touch()

            return f"File created successfully: {file_path}"

        except Exception as e:
            return f"Error creating file: {e}"