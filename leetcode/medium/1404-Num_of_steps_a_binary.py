"""
    Leetcode #1404
"""


class Solution:
    def numSteps(self, s: str) -> int:
        if s == "":
            return 0

        dec = 0
        i = 0
        for j in reversed(s):
            if j != "0":
                dec += (2**i)
            i += 1

        steps = 0
        while dec != 1:
            if dec % 2 == 0:
                dec //= 2
                steps += 1
            else:
                dec = dec + 1
                steps += 1

        return steps

    def numSteps_no_dec(self, s: int) -> int:
        count = 0
        carry = 0
        # below will don't do any manipulation
        # just counting operations/steps
        for i in range(len(s)-1, 0, -1):
            count += 1
            if (ord(s[i]) - ord('0') + carry) == 1:
                carry = 1
                count += 1

        return count + carry


if __name__ == "__main__":

    solution = Solution()

    assert solution.numSteps("1101") == 6
    assert solution.numSteps("10") == 1

    assert solution.numSteps_no_dec("1101") == 6
    assert solution.numSteps_no_dec("10") == 1

