"""
    Leetcode #19
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None

        tmp = head
        length = 0
        while (tmp):
            length += 1
            tmp = tmp.next

        if n > length:
            return head

        if n == length:
            return head.next

        tmp = head
        i = 0
        while i < (length - n + 1):
            if i == (length - n - 1):
                tmp.next = tmp.next.next
                break

            tmp = tmp.next
            i += 1

        return head

    def removeNthFromEnd_SINGLE_PASS(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        fast = slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next



if __name__ == "__main__":

    def printll(ll: ListNode):
        while ll:
            print(ll.val, end='->')
            ll = ll.next

        print()

    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)
    ll1.next.next.next = ListNode(4)
    ll1.next.next.next.next = ListNode(5)


    solution = Solution()
    printll(solution.removeNthFromEnd(ll1, 5))
    printll(solution.removeNthFromEnd_SINGLE_PASS(ll1, 2))

