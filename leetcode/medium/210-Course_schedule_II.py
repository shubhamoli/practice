"""
    Leetcode #210
"""

from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses < 1:
            return []

        if not prerequisites:
            return [i for i in range(numCourses)]

        # 0: unlearned, 1: learning, 2: learned
        self.course_status = [0] * numCourses   # analogous to visited arr

        # Collect advanced course for base course
        self.course_dict = defaultdict(set)     # analogous to graph
        for a, b in prerequisites:
            self.course_dict[a].add(b)


        self.course_order = []
        for course in range(numCourses):
            if not self.dfs(course):
                return []

        return self.course_order

    def dfs(self, course):
        if self.course_status[course] == 1:
            # we are already in "learning" state for this course
            # and encountered same again means, there is a cycle
            return False

        if self.course_status[course] == 2:
            return True

        # mark course as learning (from unlearned)
        self.course_status[course] = 1

        # for each pre-req of a course, check if can be completed
        for pre in self.course_dict[course]:
            if not self.dfs(pre):
                return False

        # mark course as learned (from learning)
        self.course_status[course] = 2
        # and append in order array
        self.course_order.append(course)

        return True


if __name__ == "__main__":

    solution = Solution()

    assert solution.findOrder(2, [[1, 0]]) == [0, 1]
    assert solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0, 1, 2, 3]

