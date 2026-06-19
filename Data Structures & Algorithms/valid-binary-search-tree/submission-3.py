# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, valueRange):
            if root == None:
                return True
            curr = root.val > valueRange[0] and root.val < valueRange[1]
            if curr:
                left = helper(root.left, [max(valueRange[0], -1001), root.val])
                right = helper(root.right, [root.val, min(valueRange[1], 1001)])
                return left and right
            return False
        return helper(root, [-1001, 1001])
                
