class ReadFileTool:
    def run(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return {"status": "success", "path": path, "content": content}
