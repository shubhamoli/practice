"""
    Leetcode #1438
"""

from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ, maxQ = deque(), deque()

        i = 0
        maxLen = 0
        for j in range(len(nums)):
            while minQ and minQ[-1] > nums[j]:
                minQ.pop()
            minQ.append(nums[j])

            while maxQ and maxQ[-1] < nums[j]:
                maxQ.pop()
            maxQ.append(nums[j])

            if maxQ[0] - minQ[0] <= limit:
                maxLen = max(maxLen, j - i +1)

            else:
                if maxQ[0] == nums[i]:
                    maxQ.popleft()
                if minQ[0] == nums[i]:
                    minQ.popleft()
                i += 1

        return maxLen


if __name__ == "__main__":

    solution = Solution()

    assert solution.longestSubarray([8,2,4,7], 4) == 2
    assert solution.longestSubarray([4,2,2,2,4,4,2,2], 0) == 3
