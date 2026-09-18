# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
from collections import deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        colsDict = defaultdict(list)
        colMin = float("inf")
        colMax = float("-inf")

        queue = deque([(0, root)])

        while queue:
            queue_len = len(queue)

            for i in range(queue_len):
                col, curr = queue.popleft()
                colMin = min(colMin, col)
                colMax = max(colMax, col)

                colsDict[col].append(curr.val)

                if curr.left:
                    queue.append((col-1, curr.left))
                if curr.right:
                    queue.append((col+1, curr.right))

        return [colsDict[index] for index in range(colMin, colMax+1)]

