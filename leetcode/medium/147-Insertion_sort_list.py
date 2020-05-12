"""
    Leetcode #147
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        res = ListNode(0)
        curr = res.next = head

        while curr and curr.next:
            # if next is greater move to next
            # no need to do anything
            if curr.next.val > curr.val:
                curr = curr.next
            else:
                nxt = curr.next
                curr.next = nxt.next
                pre = res
                while pre.next and pre.next.val < nxt.val:
                    pre = pre.next
                nxt.next = pre.next
                pre.next = nxt

        return res.next

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

    printll(Solution().insertionSortList(ll))   # 1->2->3->4
