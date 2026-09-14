# A stack is a "last in, first out" container.
# A Python list is already a perfect stack: append() to push, pop() to pop.
my_stack = []

my_stack.append(5)
my_stack.append(20)
my_stack.append(-7)
print(my_stack)          # [5, 20, -7]

item = my_stack.pop()    # takes the LAST item
print('Popped:', item)   # -7
print(my_stack)          # [5, 20]

my_stack.pop()
print(my_stack)          # [5]

# By popping index 0 instead, the list behaves as a queue (first in, first out).
queue = [5, 20, -7, 8, 14]
queue.pop(0)
queue.pop(0)
print(queue)             # [-7, 8, 14]
