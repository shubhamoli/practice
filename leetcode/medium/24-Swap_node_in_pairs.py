"""
    Leetcode #24
"""


from leetcode.utils import ListNode, printLL, generateLL


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return

        res = ListNode(0)
        res.next = head

        cur = res

        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first

            cur = cur.next.next

        return res.next


if __name__ == "__main__":

    solution = Solution()

    ll = generateLL([1, 2, 3, 4])

    printLL(solution.swapPairs(ll))
