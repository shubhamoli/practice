"""
    Leetcode #143
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        slow = head
        fast = head.next

        if not fast:
            return None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        stk = []
        while slow:
            _tmp = slow.next
            slow.next = None
            stk.append(slow)
            slow = _tmp

        tmp = head
        while stk and tmp:
            _tmp = tmp.next
            tmp.next = stk.pop()
            tmp.next.next = _tmp
            tmp = _tmp




if __name__ == "__main__":

    def printll(ll):
        while ll:
            print(ll.val, end="->")
            ll = ll.next
        print()

    solution = Solution()

    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)

    solution.reorderList(ll)
    printll(ll)

