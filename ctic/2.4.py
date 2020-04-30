"""
    2.4 - Write a function to partiion a LL around "x" such that values
            less than x comes nefore it and values greater than it comes after "x"
"""

# Definition of a list node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def partition(head: ListNode, x:int) -> ListNode:
    before = ListNode(0)
    b_tmp = before

    after = ListNode(0)
    a_tmp = after

    curr = head

    while curr:
        if curr.val < x:
            b_tmp.next = curr
            b_tmp = b_tmp.next
        else:
            a_tmp.next = curr
            a_tmp = a_tmp.next

        curr = curr.next

    a_tmp.next = None
    b_tmp.next = after.next

    return before.next



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

    printll(partition(ll, 5))
