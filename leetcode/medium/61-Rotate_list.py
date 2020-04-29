"""
    Leetcode #61
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        tmp = head
        length = 0
        while tmp:
            length += 1
            tmp = tmp.next

        # complete rotation
        rotate = k % length

        if rotate == 0 or not k:
            return head

        fast = head
        slow = head

        i = 0
        while i < rotate:
            fast = fast.next
            i += 1

        while fast.next:
            slow = slow.next
            fast = fast.next

        tmp = slow.next

        # Make last
        # 1 -> 2 -> 3 (slow) -> None
        slow.next = None

        # make original last point to head
        # 5 (fast) -> 1 (head) -> 2 -> 3
        fast.next = head

        # next to slow is new head
        # 4 (tmp) -> 5->1->2->3
        head = tmp

        return head


if __name__ == "__main__":

    def printll(ll):
        while ll:
            print(ll.val, end="->")
            ll = ll.next
        print()


    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)
    ll1.next.next.next = ListNode(4)
    ll1.next.next.next.next = ListNode(5)

    printll(Solution().rotateRight(ll1, 2))


