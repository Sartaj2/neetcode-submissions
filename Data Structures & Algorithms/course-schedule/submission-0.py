from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Building adjacency list for all courses
        courseMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            courseMap[crs].append(pre)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if courseMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in courseMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            courseMap[crs] = []  # Mark as checked, so further searches are fast
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
