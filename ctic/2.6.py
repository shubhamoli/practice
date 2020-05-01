"""
    2.6 - Check if a LL is palindrome or not
"""

# Definition of ListNode
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# O(n) time and space
def palindromList(head: ListNode) -> bool:
    stack = []
    tmp = head

    while tmp:
        stack.append(tmp.val)
        tmp = tmp.next

    tmp = head
    while tmp:
        if tmp.val != stack.pop():
            return False
        tmp = tmp.next

    return True


# O(n) time and O(1) space
def palindromList_constant_space(head: ListNode) -> bool:
        if not head:
            return False

        if not head.next:
            return True

        def reversell(mid: ListNode) -> ListNode:
            prev = None;
            tmp = mid
            while tmp:
                next = tmp.next;
                tmp.next = prev;
                prev = tmp;
                tmp = next;

            return prev;


        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        reverseHead = reversell(slow)

        curr = head
        rev = reverseHead

        while curr and rev:
            if curr.val != rev.val:
                return False
            curr = curr.next
            rev= rev.next

        return True


if __name__ == "__main__":

    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(1)

    ll2 = ListNode(1)
    ll2.next = ListNode(2)
    ll2.next.next = ListNode(3)

    assert palindromList(ll1) == True
    assert palindromList(ll2) == False

    assert palindromList_no_explicit_space(ll1) == True
    assert palindromList_no_explicit_space(ll2) == False
