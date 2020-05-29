"""
    Leetcode 1432
"""


class Solution:
    def maxDiff(self, num: int) -> int:
        a = b = str(num)

        # maximize 'a' by replacing left-most by 9
        # if left most is already 9 then next left
        for d in a:
            if d != '9':
                a = a.replace(d, '9')
                break

        # minimize 'b' by replacing left most by 1  (as leftmost 0 is not allowed)
        # if left most is already 1, then replace next left by 0 (if not already 0 and 1)
        if b[0] != '1':
            b = b.replace(b[0], '1')
        else:
            for d in b[1:]:
                if d not in '01':
                    b = b.replace(d, '0')
                    break

        return int(a) - int(b)


if __name__ == "__main__":

    solution = Solution()

    assert solution.maxDiff(555) == 888
    assert solution.maxDiff(123456) == 820000
    assert solution.maxDiff(9288) == 8700
