"""
    2.2 - Write a function to find Kth largest node from end in a LL
"""


# definition of ListNode
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


def findKFromLast(head: ListNode, k) -> ListNode:
    if not head:
        return None

    if not head.next:
        return head

    if not k:
        return head

    # can also put a check that
    # K can't be greater than lenght of linked list
    slow = fast = head

    i = 0
    while i < k:
        fast = fast.next
        i += 1

    while fast:
        slow = slow.next
        fast = fast.next


    return slow.val


if __name__ == "__main__":


    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)
    ll1.next.next.next = ListNode(4)
    ll1.next.next.next.next = ListNode(5)

    assert findKFromLast(ll1, 1) == 5
    assert findKFromLast(ll1, 2) == 4
    assert findKFromLast(ll1, 3) == 3
    assert findKFromLast(ll1, 5) == 1

