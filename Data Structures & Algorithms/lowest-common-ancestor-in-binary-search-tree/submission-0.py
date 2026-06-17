# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        tempP = root
        tempQ = root
        pStack = []
        qStack = []
        while tempP.val != p.val or tempQ.val != q.val:
            if tempP.val != p.val:
                pStack.append(tempP)
                if tempP.val > p.val:
                    tempP = tempP.left
                else:
                    tempP = tempP.right
            if tempQ.val != q.val:
                qStack.append(tempQ)
                if tempQ.val > q.val:
                    tempQ = tempQ.left
                else:
                    tempQ = tempQ.right
        
        pStack.append(tempP)
        qStack.append(tempQ)

        if len(pStack) >= len(qStack):
            longerStack = pStack
            shorterStack = qStack
        else:
            longerStack = qStack
            shorterStack = pStack
        
        while longerStack:
            ancestor = longerStack.pop()
            if ancestor in shorterStack:
                return ancestor
        return None