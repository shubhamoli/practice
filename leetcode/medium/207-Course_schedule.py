"""
    Leetcode #207
"""


from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        # 0: unlearned, 1: learning, 2: learned
        self.course_status = [0] * numCourses

        # Collect advanced course for base course
        self.course_dict = defaultdict(set)
        for a, b in prerequisites:
            self.course_dict[b].add(a)

        for course in range(numCourses):
            if self.dfs_is_cycle(course):
                return False

        return True

    def dfs_is_cycle(self, course):
        if self.course_status[course] == 1:
            return True
        if self.course_status[course] == 2:
            return False

        # mark this course as learning
        self.course_status[course] = 1

        for adv in self.course_dict[course]:
            if self.dfs_is_cycle(adv): return True

        # mark this course as learned
        self.course_status[course] = 2

        return False


if __name__ == "__main__":

    solution = Solution()

    assert solution.canFinish(2, [[1, 0]]) == True
    assert solution.canFinish(2, [[0, 1]]) == True
    assert solution.canFinish(2, [[1, 0], [0, 1]]) == False

