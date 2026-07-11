class CreateFileTool:
    def run(self, path: str, content: str = ""):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return {"status": "success", "path": path}
