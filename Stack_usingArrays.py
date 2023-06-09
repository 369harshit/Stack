class StackUsingArray:
    def __init__(self):
        self.stack = []

    # Method to append the element in the stack at top position.
    def push(self, element):
        self.stack.append(element)

    # Method to Pop last element from the top of the stack
    def pop(self):
        if not self.isEmpty():
            lastElement = self.stack[-1]  # Save the last element to return
            del (self.stack[-1])  # Remove the last element
            return lastElement
        else:
            return "Stack Already Empty"

    # Method to check if stack is empty or not
    def isEmpty(self):
        return self.stack == []

    def printStack(self):
        print(self.stack)


# Driver code for pro players only :), BTY it is noob friendly.
if __name__ == "__main__":
    s = StackUsingArray()
    print("*" * 5 + " Stack Using Array  " + 5 * "*")
    while True:
        el = int(input("1 for Push\n2 for Pop\n3 to check if it is Empty\n4 to print Stack\n5 to exit\n"))
        if el == 1:
            item = input("Enter Element to push in stack\n")
            s.push(item)
        if el == 2:
            print(s.pop())
        if el == 3:
            print(s.isEmpty())
        if el == 4:
            s.printStack()
        if el == 5:
            break
