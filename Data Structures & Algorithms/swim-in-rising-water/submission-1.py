class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neibourRow, neighbourCol = r + dr, c + dc
                if (neibourRow < 0 or neighbourCol < 0 or
                    neibourRow == N or neighbourCol == N or
                    (neibourRow, neighbourCol) in visit
                ):
                    continue
                visit.add((neibourRow, neighbourCol))
                heapq.heappush(minHeap, [max(t, grid[neibourRow][neighbourCol]), neibourRow, neighbourCol])