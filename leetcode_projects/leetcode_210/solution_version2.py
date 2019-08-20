from typing import List


class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List:
        """首先处理入度为0的所有节点/课程（没有先修课程）。如果从图中删除所有这些课程，以及它们的出边，
        就可以找到下一步应该处理的课程/节点。这些节点也是入度为0的节点。重复这样做，直到所有的课程都被考虑在内。"""
        self._init_course_info(numCourses, prerequisites)
        independent_course = self._get_independent_course()

        while independent_course:
            course = independent_course.pop(0)
            self.marked[course] = True
            self.ordered_courses.append(course)
            self._change_neighbor_courses(course, independent_course)

        if not all(self.marked):
            return []

        return self.ordered_courses

    def _change_neighbor_courses(self, course, independent_course):
        for nxt_course in self.couse_table[course]:
            if self.marked[nxt_course]:
                continue
            self.end_degree[nxt_course] -= 1
            if self.end_degree[nxt_course] == 0:
                independent_course.append(nxt_course)

    def _get_independent_course(self):
        independent_course = []
        for course, degree in enumerate(self.end_degree):
            if degree == 0:
                independent_course.append(course)
        return independent_course

    def _init_course_info(self, numCourses, prerequisites):
        self.ordered_courses = []  # 拓扑排序结果
        self.couse_table = [[] for _ in range(numCourses)]  # 课程的图结构
        self.end_degree = [0] * numCourses  # 存储每门课程的入度
        self.marked = [False] * numCourses  # 已经修过过的课程

        for course1, course2 in prerequisites:
            self.couse_table[course2].append(course1)
            self.end_degree[course1] += 1


def test():
    s = Solution()
    assert s.findOrder(2, [[1, 0]]) == [0, 1]
    assert s.findOrder(3, [[1, 0], [1, 2], [0, 1]]) == []
    assert s.findOrder(2, [[1, 0], [0, 1]]) == []
    assert s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) in ([0, 2, 1, 3], [0, 1, 2, 3])


if __name__ == '__main__':
    test()
