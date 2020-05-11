"""
    Leetcode #139
"""


from typing import List

class Solution:
    status = False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False

        if not wordDict:
            return False

        def helper(s, memo):
            if memo.get(s) is not None:
                return memo[s]

            if not s:
                return True

            for word in wordDict:
                if s[:len(word)] != word:
                    continue

                if helper(s[len(word):], memo):
                    memo[s] = True
                    return True

            memo[s] = False
            return False

        return helper(s, {})

if __name__ == "__main__":

    solution = Solution()

    assert solution.wordBreak("leetcode", ["leet", "code"]) == True
    assert solution.wordBreak("applepenapple", ["apple", "pen"]) == True
    assert solution.wordBreak("catsandog", ["cats",  "and", "dogs"]) == False
    assert solution.wordBreak("aaaaaaa", ["aaaa",  "aaa"]) == True
