"""
    2.8 - Detect loop in LL
"""


# Definition of ListNode
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Floyd' algorithm
def detectLoop(head: ListNode) -> bool:
    if not head or not head.next:
        return False

    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            # Also you can write logic to remove loop
            return True

    return False


if __name__ == "__main__":

    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)

    ll2 = ListNode(1)
    ll2.next = ListNode(2)
    ll2.next.next = ll2

    assert detectLoop(ll1) == False
    assert detectLoop(ll2) == True



