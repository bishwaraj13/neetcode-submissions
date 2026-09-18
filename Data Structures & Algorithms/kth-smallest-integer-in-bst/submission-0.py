# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        result = None

        def dfs(root):
            nonlocal cnt, result

            if not root:
                return None

            dfs(root.left)
            cnt -= 1
            if cnt == 0:
                result = root.val
                return

            dfs(root.right)

        dfs(root)
        return result