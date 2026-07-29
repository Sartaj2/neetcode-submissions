# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0   # instance of class self used for calculating diameter
        
        # Returns Height 
        def depthforsearch(current):
            if not current:
               return 0
            
            left = depthforsearch(current.left)
            right = depthforsearch(current.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)  # if we dont add one then we are calculating max of either of subtree if added one then calculating max height from current
        
        depthforsearch(root)
        return self.res