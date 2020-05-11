"""
    Leetcode #138
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        cache = dict()
        def helper(node):
            if not node:
                return (None)

            if node in cache:
                return (cache[node])

            n = Node(node.val)
            cache[node] = n

            n.next = helper(node.next)
            n.random = helper(node.random)

            return n

        return helper(head)


if __name__ == "__main__":

    def printll(ll):
        while ll:
            print(ll.val, end="->")
            ll = ll.next

        print()

    ll = Node(7)
    ll.next = Node(13)
    ll.next.next = Node(11)
    ll.next.next.next = Node(10)
    ll.next.next.next.next = Node(1)

    ll.next.random = ll
    ll.next.next.random = ll.next.next.next.next
    ll.next.next.next.random = ll.next.next
    ll.next.next.next.next.random = ll

    res = Solution().copyRandomList(ll)
    printll(res)

