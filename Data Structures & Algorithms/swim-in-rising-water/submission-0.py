from typing import List
import heapq


class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # dist[r][c] stores the minimum water level required
        # to reach cell (r, c) from the top-left cell.
        #
        # Unlike normal Dijkstra where path cost is the sum
        # of edge weights, here the path cost is the maximum
        # elevation encountered along the path.
        dist = [[float("inf")] * n for _ in range(n)]

        # To stand on the starting cell, the water level must
        # be at least equal to grid[0][0].
        dist[0][0] = grid[0][0]

        # Min-heap stores:
        # (minimum water level required, row, column)
        #
        # The cell requiring the smallest water level
        # will always be processed first.
        min_heap = [(grid[0][0], 0, 0)]

        # Possible movements:
        # down, up, right, left
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while min_heap:

            # Get the cell that currently requires
            # the minimum water level to reach.
            cost, r, c = heapq.heappop(min_heap)

            # If we reached the bottom-right cell,
            # 'cost' is guaranteed to be the minimum possible
            # water level because Dijkstra always processes
            # the smallest cost first.
            if r == n - 1 and c == n - 1:
                return cost

            # This heap entry may be outdated.
            #
            # Example:
            # We may have previously added this cell with cost 10,
            # but later found a better path with cost 7.
            #
            # In that case, when cost 10 is popped,
            # we should ignore it.
            if cost > dist[r][c]:
                continue

            # Explore all 4 neighboring cells.
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Make sure the neighbor is inside the grid.
                if 0 <= nr < n and 0 <= nc < n:

                    # To move to the neighbor, the water level
                    # must be high enough for:
                    #
                    # 1. All cells visited so far -> represented by 'cost'
                    # 2. The new cell's elevation -> grid[nr][nc]
                    #
                    # Therefore, the required water level is
                    # the maximum of these two values.
                    new_cost = max(cost, grid[nr][nc])

                    # If this path reaches the neighbor with a
                    # smaller required water level, update it.
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost

                        # Add the improved path to the min-heap.
                        heapq.heappush(
                            min_heap,
                            (new_cost, nr, nc)
                        )

        # According to the problem constraints, a path always exists,
        # so normally this line will never be reached.
        return -1