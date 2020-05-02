"""
    3.2 - Write a stack with constant time push(), pop() and min() opeation
            Where min() will return minimum item in stack
"""


class StackWithMin():
    def __init__(self):
        self.minStack = []
        self.auxStack = []

    def push(self, item) -> int:
        # if new item is less than latest min
        # then, push it it min stack too
        if item < self.min():
            self.minStack.append(item)

        self.auxStack.append(item)

    def pop(self) -> int:
        item = self.auxStack.pop()
        # if popped item in current min
        # then pop it from minStack to update current min
        if item == self.min():
            self.minStack.pop()
        return item

    def min(self) -> int:
        if not self.minStack:
            return 247144554205     # a large number

        return self.minStack[-1]



if __name__ == "__main__":

    stk = StackWithMin()

    stk.push(5)
    stk.push(4)
    stk.push(7)
    stk.push(3)
    stk.push(6)

    assert stk.min() == 3

    stk.pop()
    stk.pop()   # this will pop current min 3

    assert stk.min() == 4

