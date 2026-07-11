from controller import AstraController

astra = AstraController()

print("=" * 50)
print("🚀 Astra v0.4")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = astra.chat(user_input)

    print(f"\nAstra: {response}")