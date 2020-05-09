"""
    Leetcode #131
"""


from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return s

        res = []

        def isPalindrome(st):
            return st == st[::-1]

        def helper(curr, idx):
            if idx == len(s)+1:
                res.append(curr[:])
                return

            for i in range(idx, len(s)+1):
                st = s[idx-1:i]
                # if substring is palindrome
                # push it into result
                if st == st[::-1]:
                    curr.append(st)
                    helper(curr, i+1)
                    curr.pop()


        helper([], 1)
        return res


if __name__ == "__main__":

    print(Solution().partition("aab"))      # [ ["aa","b"], ["a","a","b"] ]
