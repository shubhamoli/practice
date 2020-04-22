"""
    Leetcode #6
"""


class Solution():
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # for numRows=3 and index i = 0, next element
        # will be at i + 4
        indexDiff =  2 * numRows - 2
        res = []

        for i in range(numRows):
            d = i
            while (d < len(s)):
                res.append(s[d])

                # if not top and bottom row
                if i != 0 and i != numRows - 1 and (d + indexDiff - 2*i) < len(s):
                    res.append(s[d + indexDiff - 2*i])

                d += indexDiff

        return "".join(res)


if __name__ == "__main__":

    solution = Solution()

    assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
