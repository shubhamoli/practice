"""
    Leetcode #282
"""


from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if num == "":
            return []

        N = len(num)
        res = []
        def helper(idx, curr, value, prev_num):
            if idx >= len(num):
                if value == target:
                    res.append(curr)
                return None

            for j in range(idx+1, len(num)+1):

                string = num[idx:j]
                number = int(string)

                # avoid "00*"
                if string != "0" and num[idx] == "0":
                    continue

                if not curr:
                    helper(j, string, number, number)
                else:
                    helper(j, curr + "+" + string, value + number, number)
                    helper(j, curr + "-" + string, value - number, -number)
                    helper(j, curr + "*" + string, value - prev_num + (prev_num * number), prev_num * number)

        helper(0, "", 0, 0)
        return res


if __name__ == "__main__":

    solution = Solution()

    print(solution.addOperators("123", 6)) # ["1+2+3", "1*2*3"]
    print(solution.addOperators("232", 8)) # ["2*3+2", "2+3*2"]

