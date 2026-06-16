# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        def treesEqual(p, q):
            if p == None and q == None:
                return True
            elif p == None or q == None:
                return False
            return p.val == q.val and treesEqual(p.right, q.right) and treesEqual(p.left, q.left)
        if treesEqual(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)