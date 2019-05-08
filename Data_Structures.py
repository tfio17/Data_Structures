#
#
## Tom
#
#
## Data Structures
#
# let's start with simple stacks and queues

from collections import deque

# here is a simple stack
stack1 = list()

stack1.append('test')
stack1.append(2)
stack1.append('test2')

print("first let's have a look at stacks")
print(stack1.pop())
print(stack1.pop())


# now let's see a queue

queue = deque()
queue.append('test')
queue.append(2)
queue.append('test2')

print("now we look at queues")
print(queue.popleft())
print(queue.popleft())
