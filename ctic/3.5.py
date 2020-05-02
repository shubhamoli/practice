"""
    3.5 - Sort the stack such that smallest item is on top
"""


class Stack():

    def __init__(self):
        self.stk = []

    def push(self, item):
        self.stk.append(item)

    def pop(self):
        if self.stk:
            return self.stk.pop()
        return None

    def sortStack(self):
        tmp = []
        while self.stk:
            item = self.stk.pop()
            # if item is larger in tmp
            # then pop it from tmp and push it to self.stk
            # so that item can be pushed to desired location
            while tmp and tmp[-1] > item:
                self.stk.append(tmp.pop())

            tmp.append(item)

        while tmp: self.stk.append(tmp.pop())

    def printStack(self):
        for i in reversed(self.stk):
            print(i)
        print("---")

if __name__ == "__main__":

    stk = Stack()

    stk.push(1)
    stk.push(2)
    stk.push(3)

    stk.printStack()
    stk.sortStack()
    print(stk.pop())    # 1
