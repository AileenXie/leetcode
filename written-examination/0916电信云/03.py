class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self,val):
        self.stack.append(val)
        if not self.min or self.min[-1]>=val:
            self.min.append(val)

    def pop(self):
        if not self.stack:
            return -1
        top = self.stack[-1]
        if top==self.min[-1]:
            self.min.pop()
        self.stack.pop()
        return top

    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    def getMin(self):
        if not self.stack:
            return -1
        return self.min[-1]


ss=MinStack()
n = int(input())
for _ in range(n):
    line = list(input().strip().split())
    if line[0] == "push":
        ss.push(int(line[1]))
    elif line[0] == "pop":
        ss.pop()
    elif line[0] == "top":
        print(ss.top())
    elif line[0] == "getMin":
        print(ss.getMin())
    # print(ss.stack)
    # print(ss.min)


