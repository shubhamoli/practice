"""
    Leetcode #2
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:

    # Making class attrbutes so that
    # You don't have to pass them in recursion
    res = ListNode(0)
    head = res
    carry = 0

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            if self.carry:
                self.head.next = ListNode(self.carry)

            return

        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + self.carry

        self.carry, result = divmod(total, 10)
        self.head.next = ListNode(result)
        self.head = self.head.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        self.addTwoNumbers(l1, l2)

        return self.res.next



if __name__ == "__main__":

    def printll(ll: ListNode):
        while (ll):
            print(ll.val, end="->")
            ll = ll.next

        print()

    ll1 = ListNode(2)
    ll1.next = ListNode(4)
    ll1.next.next = ListNode(3)

    ll2 = ListNode(5)
    ll2.next = ListNode(6)
    ll2.next.next = ListNode(4)

    printll(Solution().addTwoNumbers(ll1, ll2))

