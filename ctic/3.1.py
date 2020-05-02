"""
    3.1 - Describe how would you use single array for 3 stacks
"""


class KStacks():

    def __init__(self, k, n):
        self.k = k      # no. of stacks
        self.n = n      # total size of all k stacks

        self.arr = [0]*n

        self.top = [1]*k
        self.free = 0

        self.next = [i + 1 for i in range(self.n)]
        self.next[self.n - 1] = -1

    def isFull(self):
        return self.free == -1

    def isEmpty(self, k):
        return self.top[k] == -1

    def push(self, item, k):
        if self.isFull():
            raise Exception("Stack Overdflow")

        insert_at = self.free
        self.free = self.next[self.free]
        self.arr[insert_at] = item
        self.next[insert_at] = self.top[k]
        self.top[k] = insert_at

    def pop(self, k):
        if self.isEmpty(k):
            raise None

        top_of_stack = self.top[k]
        self.top[k] = self.next[self.top[k]]
        self.next[top_of_stack] = self.free
        self.free = top_of_stack

        return self.arr[top_of_stack]

    def printStack(self, k):
        top_index = self.top[k]
        while (top_index != -1):
            print(self.arr[top_index])
            top_index = self.next[top_index]



if __name__ == "__main__":

    # Create 3 stacks using an
    # array of size 10.
    kstacks = KStacks(3, 10)

    # Push some items onto stack number 2.
    kstacks.push(15, 2)
    kstacks.push(45, 2)

    # Push some items onto stack number 1.
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)

    # Push some items onto stack number 0.
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)

    print("Popped element from stack 2 is " +
                         str(kstacks.pop(2)))
    print("Popped element from stack 1 is " +
                         str(kstacks.pop(1)))
    print("Popped element from stack 0 is " +
                         str(kstacks.pop(0)))

    kstacks.printStack(0)
