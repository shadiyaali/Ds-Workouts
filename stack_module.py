from queue import LifoQueue

stack = LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)
print(stack.get())
print(list(stack.queue))