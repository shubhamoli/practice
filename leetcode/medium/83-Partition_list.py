"""
    Leetcode #86
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None

        if not head.next:
            return head

        before = ListNode(0)
        b_tmp = before

        after = ListNode(0)
        a_tmp = after

        curr = head
        while curr:
            # here beware, that don't put <=
            # as in ques. it is stated that
            # all nodes less than x come before nodes greater than or equal to x
            if curr.val < x:
                b_tmp.next = curr
                b_tmp = b_tmp.next
            else:
                a_tmp.next = curr
                a_tmp = a_tmp.next

            curr = curr.next

        a_tmp.next = None
        b_tmp.next = after.next

        return before.next


if __name__ == "__main__":

    def printll(ll: ListNode):
        while ll:
            print(ll.val, end="->")
            ll = ll.next
        print()

    ll = ListNode(1)
    ll.next = ListNode(4)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(2)
    ll.next.next.next.next = ListNode(5)
    ll.next.next.next.next.next = ListNode(2)

    printll(Solution().partition(ll, 3))
