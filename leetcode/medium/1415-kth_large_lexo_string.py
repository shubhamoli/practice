"""
    Leetcode #1415
"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        res = []

        def helper(curr, count):
            if count == n:
                res.append("".join(curr))
                return

            for c in letters:
                if count > 0:
                    if c != curr[-1]:
                        curr.append(c)
                        helper(curr, count+1)
                        curr.pop()
                else:
                    curr.append(c)
                    helper(curr, count+1)
                    curr.pop()


        helper([], 0)

        return "" if k - 1 >= len(res) else res[k-1]


if __name__ == "__main__":

    solution = Solution()

    assert solution.getHappyString(1, 3) == "c"
    assert solution.getHappyString(1, 4) == ""
    assert solution.getHappyString(3, 9) == "cab"
