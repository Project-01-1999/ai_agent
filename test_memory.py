from memory.memory_manager import MemoryManager

memory = MemoryManager()

print(memory.remember("name", "Dinesh"))

print(memory.recall("name"))

print(memory.forget("name"))

print(memory.recall("name"))