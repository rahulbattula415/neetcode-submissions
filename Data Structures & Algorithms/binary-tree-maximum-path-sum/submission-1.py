# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def helper(root):
            if root == None:
                return 0
            
            right = helper(root.right)
            left = helper(root.left)
            right = max(0, right)
            left = max(0, left)
            res[0] = max(res[0], root.val + right + left)

            return root.val + max(right, left)
        
        helper(root)
        return res[0]
            
            
        