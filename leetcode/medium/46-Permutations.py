"""
    Leetcode #46
"""


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        store = {}
        def helper(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in nums:
                # using dict/hash for o(1) lookup
                if store.get(i): continue

                store[i] = True
                curr.append(i)

                helper(curr)

                store[i] = False
                curr.pop()

        helper([])
        return res



if __name__ == "__main__":

    solution = Solution()

    # print(solution.permute([]))
    # print(solution.permute([1]))
    print(solution.permute([1, 2, 3]))
