"""
    2.5 - Write a function to sum two numbers represented by LLs.
            Numbers are represented in reversed order
"""


from collections import deque


# Definition of a list node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def sumll(head1: ListNode, head2: ListNode) -> ListNode:
    if not head1:
        return head2

    if not head2:
        return head1

    res = tmp = ListNode(0)
    carry = 0

    while head1 or head2:
        val1 = head1.val if head1 else 0
        val2 = head2.val if head2 else 0

        result = val1 + val2 + carry
        carry, total = divmod(result, 10)
        tmp.next = ListNode(total)

        head1 = head1.next if head1 else None
        head2 = head2.next if head2 else None
        tmp = tmp.next

    if carry:
        tmp.next = ListNode(carry)

    return res.next


# recursively go to last
# and sum as usual while comming back
def sumll_FORWARD(head1: ListNode, head2: ListNode) -> ListNode:

    if not head1:
        return head2

    if not head2:
        return head1

    # to perfectly match corresponding nodes during recursion
    # we have to left pad smaller list with zero
    def length(head: ListNode) -> int:
        tmp = head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next

        return count

    def pad(head: ListNode, pad_length: int) -> ListNode:
        tmp = head
        i = 0
        while i < pad_length:
            n = ListNode(0)
            n.next = tmp
            tmp = n
            i += 1

        return tmp

    len1 = length(head1)
    len2 = length(head2)

    if len1 < len2:
        head1 = pad(head1, len2 - len1)
    if len2 < len1:
        head2 = pad(head2, len1 - len2)

    stack1 = []
    stack2 = []

    while head1 and head2:
        stack1.append(head1.val)
        stack2.append(head2.val)
        head1 = head1.next
        head2 = head2.next

    res = None
    carry = 0
    while stack1 and stack2:
        total = stack1.pop() + stack2.pop() + carry
        carry, result = divmod(total, 10)
        new = ListNode(result)
        new.next = res
        res = new

    if carry:
        tmp = ListNode(carry)
        tmp.next = res
        res = tmp

    return res



if __name__ == "__main__":

    def printll(ll):
        while ll:
            print(ll.val, end="->")
            ll = ll.next
        print()

    ll1 = ListNode(7)
    ll1.next = ListNode(1)
    ll1.next.next = ListNode(6)

    ll2 = ListNode(5)
    ll2.next = ListNode(9)
    ll2.next.next = ListNode(2)
    # below one is optional
    # it is just to check for diff length LLs
    # ll2.next.next.next = ListNode(6)

    printll(sumll(ll1, ll2))


    # for Followup part
    ll3 = ListNode(6)
    ll3.next = ListNode(1)
    ll3.next.next = ListNode(7)
    ll3.next.next.next = ListNode(9)

    ll4 = ListNode(2)
    ll4.next = ListNode(9)
    ll4.next.next = ListNode(5)
    
    printll(sumll_FORWARD(ll3, ll4))
