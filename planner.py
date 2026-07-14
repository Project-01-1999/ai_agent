class Planner:

    def create_python_project_plan(self, project_name):

        return [
            {
                "tool": "create_folder",
                "args": [project_name]
            },
            {
                "tool": "create_file",
                "args": [f"{project_name}/README.md"]
            },
            {
                "tool": "create_file",
                "args": [f"{project_name}/requirements.txt"]
            },
            {
                "tool": "create_folder",
                "args": [f"{project_name}/app"]
            },
            {
                "tool": "create_file",
                "args": [f"{project_name}/app/main.py"]
            }
        ]