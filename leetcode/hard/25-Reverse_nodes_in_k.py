"""
    Leetcode #25
"""


from leetcode.utils import ListNode, generateLL, printLL


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return

        def reverse(head, count=0):
            prev = None
            curr, _next = head, head

            while count > 0:
                _next = curr.next
                curr.next = prev
                prev = curr
                curr = _next
                count -= 1

            return (curr, prev)


        count = 0
        tmp = head

        while tmp and count < k:
            tmp = tmp.next
            count += 1

        if count < k:
            return head

        new_head, prev = reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)

        return prev


if __name__ == "__main__":

    solution = Solution()

    items = [1, 2, 3, 4, 5]
    ll = generateLL(items)

    printLL(solution.reverseKGroup(ll, 2))  # 2->1->4->3->5

    ll = generateLL(items)
    printLL(solution.reverseKGroup(ll, 3))  # 3->2->1->4->5
