class PermissionManager:

    def ask_permission(self, tool_name, target=""):

        print("\n===================================")
        print("Permission Required")
        print("-----------------------------------")
        print(f"Tool   : {tool_name}")
        print(f"Target : {target}")
        print("===================================")

        answer = input("Allow? (yes/no): ").strip().lower()

        return answer == "yes"