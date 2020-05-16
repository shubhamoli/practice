"""
    Leetcode #216
"""


from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n == 0:
            return []

        def helper(curr, idx, curr_sum):
            if len(curr) == k:
                if curr_sum == n:
                    res.append(curr[:])
                return

            if idx > 9 or len(curr) >= k:
                return

            for i in range(idx, 10):
                curr.append(i)
                helper(curr, i+1, curr_sum+i)
                curr.pop()


        res = []
        helper([], 1, 0)

        return res


if __name__ == "__main__":

    solution = Solution()

    print(solution.combinationSum3(3, 7))   # [[1, 2, 4]]
    print(solution.combinationSum3(3, 9))   # [[1,2,6], [1,3,5], [2,3,4]]
