"""
    Leetcode #496
"""

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # find next greater element for every element of nums2
        # save it in a dict
        store = {}
        stk = []
        for i in nums2:
            while stk and stk[-1] < i:
                store[stk.pop()] = i
            stk.append(i)

        res = []
        for i in nums1:
            res.append(store.get(i, -1))

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.nextGreaterElement([4,1,2], [1,3,4,2]) == [-1, 3, -1]
    assert solution.nextGreaterElement([2,4], [1,2,3,4]) == [3, -1]
