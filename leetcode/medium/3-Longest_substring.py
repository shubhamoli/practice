"""
    Leetcode #3
"""


class Solution:

    # using nested for loop on string
    def lengthOfLongestSubstring_NAIVE(self, s: str) -> int:

        store = {}
        count = 0

        # following is kinda sliding window approach
        for i in range(len(s)):

            j = i
            tmp = 0

            while j < len(s):
                if store.get(s[j]):
                    store.clear()
                    break
                else:
                    store[s[j]] = True
                    tmp += 1
                j += 1

            count = max(count, tmp)

        return count


    # Try to do this in single pass
    def lengthOfLongestSubstring(self, s: str) -> int:

        store = {}

        left = 0
        maxLen = 0

        for i, char in enumerate(s):
            if char in store and left <= store.get(char):
                left = store.get(char) + 1
            else:
                maxLen = max(maxLen, i - left + 1)

            store[char] = i

        return maxLen



if __name__ == "__main__":

    solution = Solution()

    assert solution.lengthOfLongestSubstring_NAIVE("") == 0
    assert solution.lengthOfLongestSubstring_NAIVE("a") == 1
    assert solution.lengthOfLongestSubstring_NAIVE("aaaaaa") == 1
    assert solution.lengthOfLongestSubstring_NAIVE("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring_NAIVE("abeccccabcdef") == 6

    assert solution.lengthOfLongestSubstring("") == 0
    assert solution.lengthOfLongestSubstring("a") == 1
    assert solution.lengthOfLongestSubstring("aaaaaa") == 1
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("abeccccabcdef") == 6
    assert solution.lengthOfLongestSubstring("pwwkew") == 3

