# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res

            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            # We update the res globally with maximum path sum 
            # where current node is the root
            res = max(res, root.val + leftMax + rightMax)

            # But we return root.val + leftMax/rightMax
            # because its parent can use this info
            # to compute path sum possible at their level
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res
            