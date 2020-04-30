"""
    2.1 - Write a code to remove duplicates from unsorted linked list
"""

# Definition of a ListNode
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None



def dedupe(head: ListNode) -> ListNode:
    if not head:
        return None

    if not head.next:
        return head

    store = {}
    tmp = head

    # Mark first node as True
    store[tmp.val] = True

    while tmp.next:
        if store.get(tmp.next.val):
            # remove it
            tmp.next = tmp.next.next
        else:
            store[tmp.val] = True
            tmp = tmp.next


    return head


# O(n^2) solution
# as no buffer is allowed to track occurrences
def dedupe_no_buffer(head: ListNode) -> ListNode:

    if not head:
        return None

    if not head.next:
        return head

    current = head

    # O(n^2)
    while current:
        tmp = current
        while tmp.next != None:
            if tmp.next.val == current.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        current = current.next

    return head


if __name__ == "__main__":

    def printll(ll: ListNode):
        while ll:
            print(ll.val, end="->")
            ll = ll.next
        print()


    ll1 = ListNode(1)
    ll1.next = ListNode(5)
    ll1.next.next = ListNode(2)
    ll1.next.next.next = ListNode(5)
    ll1.next.next.next.next = ListNode(5)


    printll(dedupe(ll1))
    printll(dedupe_no_buffer(ll1))
