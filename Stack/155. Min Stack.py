class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

solution = MinStack()

solution.push(5)
solution.push(3)
solution.push(7)
solution.push(2)

print("Top:", solution.top())        
print("Min:", solution.getMin())     

solution.pop()

print("Top after pop:", solution.top())     
print("Min after pop:", solution.getMin())  

