# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first element of preorder array is root
# find mid element: mid = inorder.index(root)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # The following commented logic is not optimized
        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root
        preorder_index = 0
        inorder_indexes = {v: i for i,v in enumerate(inorder)}

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            rootVal = preorder[preorder_index]
            mid = inorder_indexes[rootVal]
            preorder_index += 1

            root = TreeNode(rootVal)
            root.left = build(left, mid-1)
            root.right = build(mid+1, right)

            return root

        return build(0, len(inorder)-1)
            

