"""
    Leetcode #215
"""

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return

        if k > len(nums):
            return


        # below is similar to nlargest() method of heapq standard module

        pq = nums[:k]
        heapq.heapify(pq)   # O(k)

        for x in nums[k:]:  # O(n-k)
            if x > pq[0]:
               heapq.heappushpop(pq, x) # log(k)

        # total O(k + (n-k)log(k))
        # space O(k)

        return pq[0]



if __name__ == "__main__":

    solution = Solution()

    assert solution.findKthLargest([3,2,1,5,6,4], 2) == 5
    assert solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
