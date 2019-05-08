#
#
## Tom
#
#
## Use the linked list class

from linkedlist import *

MyList = linkedList()

MyList.insert(Node("Lars"))
MyList.insert(Node("Alex"))
print(MyList.getSize())

MyList.insert(Node("Tom"))
MyList.insert(Node("Mike"))
print(MyList.getSize())

# Use the print method
MyList.printLL()


