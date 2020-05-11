"""
    Leetcode #142
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        slow = fast = head
        found = False

        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next

            # cycle detected, but we need to find the node (where tail points to)
            if slow == fast:
                found = True
                break

        if not found:
            return None

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


if __name__ == "__main__":

    solution = Solution()

    ll = ListNode(3)
    ll.next = ListNode(2)
    ll.next.next = ListNode(0)
    ll.next.next.next = ListNode(-4)
    ll.next.next.next.next = ll.next    # cycle

    assert solution.detectCycle(ll) == ll.next

