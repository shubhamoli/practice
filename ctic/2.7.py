"""
    2.7 - Write a function to check whether two linked list intersect
          Means whether they have common node (by refernce, not by value)
"""


# Definition of ListNode
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def intersect(head1: ListNode, head2: ListNode) -> bool:
    if not head1 or not head2:
        return False

    def length(ll: ListNode) -> int:
        count = 0
        while ll:
            count += 1
            ll = ll.next

        return count

    len1 = length(head1)
    len2 = length(head2)

    # first make a common point to start
    # means, if len(ll1) > len(ll2) move len1 - len2 node ahead and vice versa
    # then compare node by node to check if they have common node

    if len1 > len2:
        i = 0
        while head1 and i < (len1 - len2):
            i += 1
            head1 = head1.next
    else:
        i = 0
        while head2 and i < (len2 - len1):
            i += 1
            head2 = head2.next

    while head1 and head2:
        if head1 == head2:
            return True

        head1 = head1.next
        head2 = head2.next

    return False


if __name__ == "__main__":

    ll1 = ListNode(1)
    ll1.next = ListNode(1)
    ll1.next.next = ListNode(1)
    ll1.next.next.next = ListNode(1)
    ll1.next.next.next.next = ListNode(1)

    ll2 = ListNode(7)
    ll2.next = ListNode(8)
    ll2.next.next = ll1.next.next.next

    assert intersect(ll1, ll2) == True

    ll1 = ListNode(1)
    ll1.next = ListNode(1)
    ll1.next.next = ListNode(1)
    ll1.next.next.next = ListNode(1)
    ll1.next.next.next.next = ListNode(1)

    ll2 = ListNode(7)
    ll2.next = ListNode(8)
    ll2.next.next = ListNode(9)

    assert intersect(ll1, ll2) == False

