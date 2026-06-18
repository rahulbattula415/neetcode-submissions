# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        if root == None:
            return []
        queue.append(root)

        levelArray = []
        retArray = []
        counter = 0
        nodesPerLevel = 1
        nodesNextLevel = 0

        while queue:
            temp = queue.pop(0)
            if temp != None:
                queue.append(temp.left)
                queue.append(temp.right)
                levelArray.append(temp.val)
                nodesNextLevel += 2
            counter += 1
            if counter == nodesPerLevel:
                counter = 0
                nodesPerLevel = nodesNextLevel
                nodesNextLevel = 0
                if levelArray != []:
                    retArray.append(levelArray)
                levelArray = []
        return retArray


            