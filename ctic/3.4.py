"""
    3.4 - Implement queue using stack data structure

    we'll be using two stacks for this
"""


class myQueue():

    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, val: int):
        self.stk1.append(val)

    # compromising pop() operation
    # O(n) instead of O(1)
    def pop(self) -> int:
        while self.stk1:
            self.stk2.append(self.stk1.pop())

        item = self.stk2.pop() if len(self.stk2) else None

        while self.stk2:
            self.stk1.append(self.stk2.pop())

        return item

    def top(self) -> int:
        return self.stk1[-1]

    def size(self) -> int:
        return len(self.stk1) + len(self.stk2)




if __name__ == "__main__":

    q = myQueue()

    q.push(1)
    q.push(2)
    q.push(3)

    assert q.pop() == 1

    q.push(4)
    q.push(5)

    assert q.pop() == 2
    assert q.top() == 5
