# We are given a set of points, but no edges between them.
# We can think of each point as a node in a graph.

# Step 1 is to create an edge between every pair of points.
# The weight/cost of an edge is the Manhattan distance between
# those two points:

# |x1 - x2| + |y1 - y2|

# Once we build this graph, the problem becomes:
# "Connect all nodes together with the minimum possible total edge cost."

# This is exactly a Minimum Spanning Tree (MST) problem,
# so we can apply Prim's algorithm.

# Prim's algorithm works by:
# 1. Starting from any node (we start from node 0).
# 2. Keeping track of all edges that can take us from the nodes
# already in our MST to nodes we have not visited yet.
# 3. Always choosing the cheapest available edge.
# 4. Adding that new node to the MST.
# 5. Adding all of that node's outgoing edges to our min-heap.
# 6. Repeating until every node has been added.

# In the code:
# - visitedPoints contains the nodes already included in the MST.
# - minHeap is a min-heap containing candidate edges in the form
# [cost, node].
# - totalCost stores the total cost of the MST.

# We initialize the heap with [0, 0], meaning:
# "Visit node 0 first, with a cost of 0."

# Each time we pop from the heap, we get the cheapest edge/node
# currently available. If that node was already visited, we skip it
# because another cheaper edge may have already connected it.

# Otherwise, we add its edge cost to the totalCost, mark the node as
# visited, and push all edges from this node to unvisited neighbors
# into the heap.

# When all N nodes have been visited, res is the minimum total
# cost required to connect all of the points.

# Its sort of like BFS + Priority Queue
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        numberOfPoints = len(points)

        adjacencyList = {pointIndex: [] for pointIndex in range(numberOfPoints)}

        for firstPointIndex in range(numberOfPoints):
            firstX, firstY = points[firstPointIndex]

            for secondPointIndex in range(firstPointIndex + 1, numberOfPoints):
                secondX, secondY = points[secondPointIndex]

                distance = (
                    abs(firstX - secondX)
                    + abs(firstY - secondY)
                )

                adjacencyList[firstPointIndex].append(
                    [distance, secondPointIndex]
                )

                adjacencyList[secondPointIndex].append(
                    [distance, firstPointIndex]
                )

        totalCost = 0
        visitedPoints = set()

        minHeap = [[0, 0]]

        while len(visitedPoints) < numberOfPoints:
            cost, pointIndex = heapq.heappop(minHeap)

            if pointIndex in visitedPoints:
                continue

            totalCost += cost
            visitedPoints.add(pointIndex)

            for neighbourCost, neighbourIndex in adjacencyList[pointIndex]:
                if neighbourIndex not in visitedPoints:
                    heapq.heappush(
                        minHeap,
                        [neighbourCost, neighbourIndex]
                    )

        return totalCost
        