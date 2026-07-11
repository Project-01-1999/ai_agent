from ollama import chat
from settings import MODEL_NAME


class LLM:

    def ask(self, prompt: str):

        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]