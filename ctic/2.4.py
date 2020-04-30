"""
    2.4 - Write a function to partiion a LL around "x" such that values
            less than x comes nefore it and values greater than it comes after "x"
"""

# Definition of a list node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def partition_stable(head: ListNode, x:int) -> ListNode:
    beforeStart = None
    beforeEnd = None
    afterStart = None
    afterEnd = None

    curr = head

    while curr:
        tmp = curr.next

        if curr.val < x:
            if beforeStart == None:
                beforeStart = curr
                beforeEnd = beforeStart
            else:
                beforeEnd.next = curr
                beforeEnd = curr
        else:
            if afterStart == None:
                afterStart = curr
                afterEnd = afterStart
            else:
                afterEnd.next = curr
                afterEnd = curr

        curr = tmp

    if beforeStart == None:
        return afterStart

    beforeStart.next = afterStart

    return beforeStart

def partition(head: ListNode, x: int) -> ListNode:

    before = head
    after = head

    curr = head
    while curr:
        tmp = curr.next
        print(curr.val)
        if curr.val < x:
            # insert current node before "head"
            curr.next = before
            before = curr
        else:
            after.next = curr
            after = curr

        curr = tmp

    after.next = None

    return before


if __name__ == "__main__":

    def printll(ll):
        while ll:
            print(ll.val, end="->")
            ll = ll.next
        print()

    # 3->5->8->5->10->2->1
    # x = 5
    ll = ListNode(3)
    ll.next = ListNode(5)
    ll.next.next = ListNode(8)
    ll.next.next.next = ListNode(5)
    ll.next.next.next.next = ListNode(10)
    ll.next.next.next.next.next = ListNode(2)
    ll.next.next.next.next.next.next = ListNode(1)

    printll(partition_stable(ll, 5))
