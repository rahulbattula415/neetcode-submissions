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
        rootValue = preorder[0]
        rootIdx = inorder.index(rootValue)
        
        leftInorder = inorder[:rootIdx]
        rightInorder = inorder[rootIdx + 1:]
        leftPreorder = preorder[1:1 + len(leftInorder)]
        rightPreorder = preorder[1 + len(leftInorder):]

        left = self.buildTree(leftPreorder, leftInorder)
        right = self.buildTree(rightPreorder, rightInorder)
        
        return TreeNode(preorder[0], left, right)

