from typing import List


class Solution:
    UNKNOWN = 0
    VISITING = 1
    VISITED = 2

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List:
        self.ordered_courses = []
        self.couse_table = [[] for _ in range(numCourses)]
        self.course_state = [Solution.UNKNOWN] * numCourses
        for course1, course2 in prerequisites:
            self.couse_table[course2].append(course1)

        for course in range(numCourses):
            if self.dfs(course):
                return []
        return self.ordered_courses

    def dfs(self, course) -> bool:
        """判断是否有环, 并做拓扑排序"""
        if self.course_state[course] == Solution.VISITED:
            return False
        if self.course_state[course] == Solution.VISITING:
            return True
        self.course_state[course] = Solution.VISITING
        for neighbor in self.couse_table[course]:
            if self.dfs(neighbor):
                return True
        self.course_state[course] = Solution.VISITED
        self.ordered_courses.insert(0, course)
        return False


def test():
    s = Solution()
    assert s.findOrder(2, [[1, 0]]) == [0, 1]
    assert s.findOrder(2, [[1, 0], [0, 1]]) == []
    assert s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) in ([0, 2, 1, 3], [0, 1, 2, 3])


if __name__ == '__main__':
    test()
