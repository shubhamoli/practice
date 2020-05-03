"""
    Leetcode #82
"""


from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        if not head.next:
            return head

        dummy = ListNode(0);  # construct a dummy node
        d = dummy

        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
            else:
                d.next = head
                d = d.next

            head = head.next

        d.next = None

        return dummy.next



if __name__ == "__main__":

    def printll(ll: ListNode):
        while ll:
            print(ll.val, end="->")
            ll = ll.next

        print()


    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)
    ll1.next.next.next = ListNode(3)
    ll1.next.next.next.next = ListNode(4)
    ll1.next.next.next.next.next = ListNode(4)
    ll1.next.next.next.next.next.next = ListNode(5)

    printll(Solution().deleteDuplicates(ll1))

    ll2 = ListNode(1)
    ll2.next = ListNode(1)
    ll2.next.next = ListNode(1)
    ll2.next.next.next = ListNode(2)
    ll2.next.next.next.next = ListNode(3)

    printll(Solution().deleteDuplicates(ll2))
