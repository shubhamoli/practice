"""
    Leetcode #127
"""


from typing import List
import collections

class Solution:
    count = 0
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # O(n)
        lookup = set(wordList)

        queue = collections.deque([beginWord])
        level = 0

        while queue:
            size, level = len(queue), level+1

            for i in range(size):
                curr = queue.popleft()

                # curr is wndWord return level
                if curr == endWord:
                    return level

                for j in range(len(curr)):
                    a, b = curr[:i], curr[i+1:]
                    # for each word generate and try all combo
                    # by changing 1 char from a to z
                    # for hit --> ait, hat, hia -- bit, hbt, hib, and so on
                    for k in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = curr[:j] + k + curr[j+1:]
                        # curr != new_word and new_word is in wordList
                        # add it to queue for futher processing
                        if new_word in lookup:
                            queue.append(new_word)
                            # remove to avoid dupes
                            # as we have already checked this
                            lookup.remove(new_word)


        return 0


if __name__ == "__main__":

    solution = Solution()

    assert solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
