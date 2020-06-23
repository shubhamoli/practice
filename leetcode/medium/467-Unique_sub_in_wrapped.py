"""
    Leetcode #467
"""


from collections import defaultdict


class Solution:

    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0

        pattern = 'abcdefghijklmnopqrstuvwxyza'

        count = defaultdict(int)
        count[p[0]] = 1

        max_len = 1

        for i in range(1, len(p)):
            if p[i-1] + p[i] in pattern:
                max_len += 1
            else:
                max_len = 1

            count[p[i]] = max(count[p[i]], max_len)

        return sum(count.values())


if __name__ == "__main__":

    solution = Solution()

    assert solution.findSubstringInWraproundString("zab") == 6

