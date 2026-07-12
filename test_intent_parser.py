from intent_parser import IntentParser

parser = IntentParser()

print(parser.parse("Create folder ShoppingApp"))
print(parser.parse("Make a file called notes.txt"))
print(parser.parse("Hello Astra"))