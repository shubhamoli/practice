"""
    Leetcode #77
"""


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(curr, idx):
            if len(curr) == k:
                res.append(curr[:])
                return

            for i in range(idx, n+1):
                curr.append(i)
                helper(curr, i+1)
                curr.pop()

        helper([], 1)
        return res


if __name__ == "__main__":

    print(Solution().combine(4, 2))
