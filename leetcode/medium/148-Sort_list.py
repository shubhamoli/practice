"""
    Leetcode #148
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head


        tmp = slow = fast = head

        while fast and fast.next:
            tmp = slow
            slow = slow.next
            fast = fast.next.next

        # mark end of first half
        # so that we don't go on end less loop
        #
        # head - begining of first half
        # tmp - end of first half
        # slow - begining of second half
        # fast - end of second half
        tmp.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        root = ListNode(None)
        tmp = root

        while left and right:
            if left.val <= right.val:
                tmp.next = left
                left = left.next
            else:
                tmp.next = right
                right = right.next

            tmp = tmp.next

        if left:
            tmp.next = left

        if right:
            tmp.next = right

        return root.next



if __name__ == "__main__":

    def printll(ll):
        while ll:
            print(ll.val, end="->")
            ll = ll.next

        print()

    ll = ListNode(4)
    ll.next = ListNode(2)
    ll.next.next = ListNode(1)
    ll.next.next.next = ListNode(3)

    printll(Solution().sortList(ll))    # 1->2->3->4

