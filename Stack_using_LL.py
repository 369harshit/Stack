# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack class
class Stack:

    # constructor initializing head with None
    def __init__(self):
        self.head = None

    # Checks if stack is empty
    def isempty(self):
        return True if self.head is None else False

    # push method adds element to the start of stack
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # returns the data of the head node
    def topElement(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    # pop method will remove the current head and return its value
    def pop(self):
        if self.isempty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data


# Driver code
Mystack = Stack()

Mystack.push(1)
Mystack.push(2)
Mystack.push(3)
Mystack.push(4)

print(Mystack.topElement())
print(Mystack.pop())

print(Mystack.topElement())
print(Mystack.pop())

print(Mystack.topElement())
print(Mystack.pop())
