"""
    Leetcode #406
"""


from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []

        people.sort(key=lambda x: (-x[0], x[1]))

        queue = []
        for p in people:
            queue.insert(p[1], p)

        return queue


if __name__ == "__main__":

    solution = Solution()

    assert solution.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]) == [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
