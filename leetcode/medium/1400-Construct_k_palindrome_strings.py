"""
    Leetcode #1400
"""


from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        count = Counter(s)
        odd = 0

	    # count odd frequencies, if odd < k then palindrome can be constructed
        for i in count:
            odd += (count[i] % 2)

        return True if odd <= k else False


if __name__ == "__main__":

    solution = Solution()

    assert solution.canConstruct("annabelle", 2) == True
    assert solution.canConstruct("leetcode", 3) == False

