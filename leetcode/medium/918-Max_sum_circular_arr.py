"""
    Leetcode 918
"""

from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if not A:
            return 0

        curr_max = curr_min = total =  0
        _max = float("-inf")
        _min = float("inf")

        # track total sum
        # minimum sum
        # maximum sum (as normally you would)
        #
        # (totalSum - minSum) can give us maxSum (for subarray crossing borders)
        for i in range(len(A)):
            total += A[i]
            curr_max = max(A[i]+curr_max, A[i])
            _max = max(_max, curr_max)
            curr_min = min(A[i]+curr_min, A[i])
            _min = min(_min, curr_min)

        # Just one to pay attention: 
        # If all numbers are negative, maxSum = max(A) and minSum = sum(A).
        # In this case, max(maxSum, total - minSum) = 0, which means the sum of an empty subarray.
        # According to the deacription, We need to return the max(A), instead of sum of am empty subarray.
        # So we return the maxSum to handle this corner case.
        return max(_max, total-_min) if _max > 0 else _max


if __name__ == "__main__":

    solution = Solution()

    assert solution.maxSubarraySumCircular([1,-2,3,-2]) == 3
    assert solution.maxSubarraySumCircular([5,-3,5]) == 10
    assert solution.maxSubarraySumCircular([3,-1,2,-1]) == 4
    assert solution.maxSubarraySumCircular([3,-2,2,-3]) == 3
    assert solution.maxSubarraySumCircular([-2,-3,-1]) == -1
