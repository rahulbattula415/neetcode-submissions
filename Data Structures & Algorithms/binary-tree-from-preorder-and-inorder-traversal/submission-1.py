# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0], None, None)
        value = preorder[0]
        leftInOrder = inorder[:inorder.index(value)]
        rightInOrder = inorder[inorder.index(value) + 1:]
        leftSubtree = self.buildTree(preorder[1:1 + len(leftInOrder)], leftInOrder)
        rightSubtree = self.buildTree(preorder[1 + len(leftInOrder):], rightInOrder)
        root = TreeNode(value, leftSubtree, rightSubtree)
        return root
