from typing import List


class Solution:
    UNKNOWN = 0
    VISITING = 1
    VISITED = 2

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.couse_table = [[] for _ in range(numCourses)]
        self.course_state = [Solution.UNKNOWN] * numCourses
        for course1, course2 in prerequisites:
            self.couse_table[course2].append(course1)

        for course in range(numCourses):
            if self.dfs(course):
                return False
        return True

    def dfs(self, course):
        """判断是否有环"""
        if self.course_state[course] == Solution.VISITED:
            return False
        if self.course_state[course] == Solution.VISITING:
            return True
        self.course_state[course] = Solution.VISITING
        for neighbor in self.couse_table[course]:
            if self.dfs(neighbor):
                return True
        self.course_state[course] = Solution.VISITED
        return False


def test():
    s = Solution()
    assert s.canFinish(2, [[1, 0]])
    assert not s.canFinish(2, [[1, 0], [0, 1]])


if __name__ == '__main__':
    test()
