# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Every node's value in BST has a range. 
# It should be higher than its left child and lower than its right child
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, low, high):
            if not root:
                return True

            if not (low<root.val<high):
                return False

            left = valid(root.left, low, root.val)
            right = valid(root.right, root.val, high)

            return left and right

        return valid(root, float("-inf"), float("inf"))
