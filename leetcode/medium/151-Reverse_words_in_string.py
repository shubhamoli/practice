"""
    Leetcode #151
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""

        res = []

        j = len(s)
        for i in range(len(s)-1,-1,-1):
            # trim the trailing space
            if s[i] == " ":
                j = i

            # if we encountered a " " before the words,
            # we know a word ended here, append " " or the word
            elif i == 0 or s[i-1] == " ":
                res.append(s[i:j])

        return " ".join(res)



if __name__ == "__main__":

    solution = Solution()

    assert solution.reverseWords("the sky is blue") == "blue is sky the"
    assert solution.reverseWords("  hello world!  ") == "world! hello"
    assert solution.reverseWords("a good   example") == "example good a"

