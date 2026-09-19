# We solve it by Topological Sort (Kahn's Algo).
# Interesting thing about Topological Sort is that its actually BFS
# Only thing is that the starting nodes are the ones that have no dependency.
# To find out starting node, we compute indegree of each node.
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjacencyList = [[] for i in range(numCourses)]

        for source, destination in prerequisites:
            indegree[destination] += 1
            adjacencyList[source].append(destination)

        q = deque()

        # All the starting nodes in queue, the ones that have no dependency
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0

        while q:
            node = q.popleft()
            finish += 1

            for neighbour in adjacencyList[node]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    q.append(neighbour)

        return finish == numCourses


        