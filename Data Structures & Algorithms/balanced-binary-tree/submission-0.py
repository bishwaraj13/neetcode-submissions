# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Instead of using a separate recursive method to call height(),
# use same dfs to compute both balanced and height
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1+max(left[1], right[1])]

        return dfs(root)[0]
              