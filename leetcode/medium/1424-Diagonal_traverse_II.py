"""
    Leetcode #1424
"""


from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if not nums or not nums[0]:
            return []

        store = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                # store diagonal values as for a diagonal
                # i+j will have same value
                store[i+j].append(nums[i][j])


        i = 0
        res = []
        # extend res for each sum starting from 0
        while store.get(i):
            # reversing to get last value first
            res.extend(reversed(store.get(i)))
            i += 1

        return res



if __name__ == "__main__":

    solution = Solution()

    nums = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    assert solution.findDiagonalOrder(nums) == [1,4,2,7,5,3,8,6,9]

    nums = [[1,2,3,4,5],
            [6,7],
            [8],
            [9,10,11],
            [12,13,14,15,16]]

    assert solution.findDiagonalOrder(nums) == [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

