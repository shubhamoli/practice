# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self._head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """

        # Reservoir Sampling
        # Why this gurantees 1/k for all
        # see this: https://www.youtube.com/watch?v=Ybra0uGEkpM
        result, node, index = self._head, self.head.next, 1
        while node:
            if random.randint(0, index) is 0:
                result = node
            node = node.next
            index += 1
        return result.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
