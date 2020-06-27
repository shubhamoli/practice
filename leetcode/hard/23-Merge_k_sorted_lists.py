"""
    Leetcode #23
"""


from typing import List
from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists_BF(self, lists: List[ListNode]) -> ListNode:
        arr = []

        for l in lists:
            tmp = l
            while tmp:
                arr.append(tmp.val)
                tmp = tmp.next

        head = tmp = ListNode(0)
        for i in sorted(arr):
            tmp.next = ListNode(i)
            tmp = tmp.next

        return head.next


    def mergeKLists_KWay(self, lists: List[ListNode]) -> ListNode:
        # to compare ListNode objects
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val

        head = tmp = ListNode(0)

        pq = PriorityQueue()

        for l in lists:
            if l:
                # first find out smallest head among k lists
                pq.put((l.val, l))

        while not pq.empty():
            val, node = pq.get()

            # smallest head will be appended in answer
            tmp.next = ListNode(val)
            tmp = tmp.next

            # move one ele ahead of this node (node with smallest head)
            node = node.next
            if node:
                pq.put((node.val, node))


        return head.next


    def mergeKLists_DIVCON(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return

        if len(lists) == 1:
            return lists[0]


        def merge(left, right):
            tmp = cur = ListNode(0)
            while left and right:
                if left.val < right.val:
                    tmp.next = left
                    left = left.next
                else:
                    tmp.next = right
                    right = right.next

                tmp = tmp.next

            tmp.next = left or right

            return cur.next

        mid = len(lists) // 2

        left = self.mergeKLists_DIVCON(lists[:mid])
        right = self.mergeKLists_DIVCON(lists[mid:])

        return merge(left, right)





if __name__ == "__main__":

    solution = Solution()

    ll1 = ListNode(1)
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)

    ll2 = ListNode(4)
    ll2.next = ListNode(5)
    ll2.next.next = ListNode(6)

    ll3 = ListNode(1)
    ll3.next = ListNode(3)
    ll3.next.next = ListNode(5)


    def printll(ll):
        while ll:
            print(ll.val, end="->")
            ll = ll.next
        print("")

    # 1->1->2->3->3->4->5->5->6
    printll(solution.mergeKLists_BF([ll1, ll2, ll3]))
    printll(solution.mergeKLists_KWay([ll1, ll2, ll3]))
    printll(solution.mergeKLists_DIVCON([ll1, ll2, ll3]))

