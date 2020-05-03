"""
    Leetcode #92
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        if not head.next:
            return head

        if m == n:
            return head

        # Skipping to m-1
        curr, prev = head, None
        i = 0

        while curr and i < m-1:
            prev = curr
            curr = curr.next
            i += 1

        # save them for later
        first = prev
        last = curr

        # iterate and reverse m to n nodes
        i = 0
        while curr and i < n - m + 1:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            i += 1

        if first:
            first.next = prev
        else:
            head = prev

        last.next = curr
        return head


if __name__ == "__main__":

    def printll(ll: ListNode):
        while ll:
            print(ll.val, end="->")
            ll = ll.next
        print()

    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)
    ll1.next.next.next = ListNode(4)
    ll1.next.next.next.next = ListNode(5)

    printll(ll1)
    printll(Solution().reverseBetween(ll1, 2, 4))
