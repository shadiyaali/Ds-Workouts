def update_stack_value(stack, index, new_value):
    temp_stack = []

    
    for i in range(index):
        temp_stack.append(stack.pop())

    
    stack.pop()
    stack.append(new_value)

    
    while len(temp_stack) > 0:
        stack.append(temp_stack.pop())
 
 
stack = [1, 2, 3, 4, 5]

 
update_stack_value(stack, 2, 10)

 
print(stack)
 
