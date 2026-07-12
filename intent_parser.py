import re


class IntentParser:

    def parse(self, message: str):

        text = message.strip()

        # Create Folder
        match = re.match(
            r"(?i)(create|make)\s+(a\s+)?folder\s+(called|named)?\s*(.+)",
            text
        )

        if match:
            return {
                "intent": "create_folder",
                "name": match.group(4).strip()
            }

        # Create File
        match = re.match(
            r"(?i)(create|make)\s+(a\s+)?file\s+(called|named)?\s*(.+)",
            text
        )

        if match:
            return {
                "intent": "create_file",
                "name": match.group(4).strip()
            }

        return {
            "intent": "chat",
            "message": text
        }
    