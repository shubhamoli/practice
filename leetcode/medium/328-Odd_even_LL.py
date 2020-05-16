"""
    Leetcode #328
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd = o = ListNode(-1)
        even = e = ListNode(-1)

        i = 1
        tmp = head
        while tmp:
            if i % 2 == 0:
                e.next = tmp
                e = tmp
            else:
                o.next = tmp
                o = tmp

            i += 1
            tmp = tmp.next

        o.next = even.next
        e.next = None

        return odd.next



if __name__ == "__main__":

    def printll(ll):
        while ll:
            print(ll.val, end="->")
            ll = ll.next

        print()


    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    ll.next.next.next.next = ListNode(5)

    printll(Solution().oddEvenList(ll))


