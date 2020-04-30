"""
    2.3 - Write a function to delete middle node of a LL
"""


# definition of ListNode
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


def deleteMiddle(head: ListNode) -> ListNode:

    if not head:
        return None

    if not head.next:
        return head

    slow = head
    fast = head.next

    # the idea is to move fast at 2x speed as slow
    # by the time fast reaches end
    # slow will reach middle node, which can be deleted
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    slow.next = slow.next.next

    return head


if __name__ == "__main__":

    def printll(ll: ListNode):
        while ll:
            print(ll.val, end="->")
            ll = ll.next
        print()

    ll1 = ListNode("a")
    ll1.next = ListNode("b")
    ll1.next.next = ListNode("c")
    ll1.next.next.next = ListNode("d")
    ll1.next.next.next.next = ListNode("e")
    ll1.next.next.next.next.next = ListNode("f")

    printll(ll1)
    printll(deleteMiddle(ll1))
