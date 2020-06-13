"""
    Leetcode #801
"""


from typing import List

class Solution:
    # A and B with non-xero length
    # A[i] and B[i] are allowed to swap (same index)
    # gurantees that for a given input it is possible
    def minSwap(self, A: List[int], B: List[int]) -> int:

        n = len(A)

        swap = [n+1] * n    # n+1 because no of swaps can't be greater the len of A
        noswap = [n+1] * n  # instead of n+1 any arbitrary large value like float("inf") can also be used

        # base cases
        noswap[0] = 0   # if we are not swapping, then min swaps = 0
        swap[0] = 1    # if we are swapping, then min swaps = 1

        for i in range(1, n):

            # no need to swap at i
            if A[i-1] < A[i] and B[i-1] < B[i]:
                noswap[i] = noswap[i-1]     # same as no. of noswap till i-1
                swap[i] = swap[i-1] + 1     # reverse previous swap

            # we can swap or not swap (both have no effect on increasing order of element)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                noswap[i] = min(noswap[i], swap[i-1])   # min(noswaps[i], swaps till i-1)
                swap[i] = min(swap[i], noswap[i-1]+1)

        return min(noswap[n-1], swap[n-1])


if __name__ == "__main__":

    solution = Solution()

    assert solution.minSwap([1,3,5,4], [1, 2, 3, 7]) == 1   # A[3] and B[3]
