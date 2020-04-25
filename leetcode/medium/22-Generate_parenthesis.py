"""
    Leetcode #22
"""


from typing import List


class Solution:
    res = []
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, path, res):
            # base case
            if l + r == 2 * n:
                res.append(path)
                return None

            if l < n:
                dfs(l + 1, r, path + '(', res)

            # This is the key
            if r < l:
                dfs(l, r + 1, path + ')', res)

        res = []
        dfs(0, 0, "", res)

        return res


if __name__ == "__main__":

    solution = Solution()

    for i in solution.generateParenthesis(3):
        print(i)

    print()
