"""
    Leetcode #5
"""


# O(n^2) solution
class Solution():
    def expandFromCenter(self, s: str, left: int, right: int) -> int:
        # loop till left and right are equal
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1

        return right - left - 1


    def longestPalindrome(self, s: str) -> str:
        if not s or (len(s) == 0):
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            # for odd
            l1 = self.expandFromCenter(s, i, i)
            # for even
            l2 = self.expandFromCenter(s, i, i+1)

            maxLen = max(l1, l2)

            if maxLen > (end - start):
                start = i - ((maxLen - 1)//2)
                end = i + (maxLen // 2)

        return s[start:end+1]



if __name__ == "__main__":

    solution = Solution()

    assert solution.longestPalindrome("") == ""
    assert solution.longestPalindrome("a") == "a"
    assert solution.longestPalindrome("bb") == "bb"
    assert solution.longestPalindrome("babab") == "babab"
    assert solution.longestPalindrome("abacdefghi") == "aba"
    assert solution.longestPalindrome("cbbd") == "bb"

