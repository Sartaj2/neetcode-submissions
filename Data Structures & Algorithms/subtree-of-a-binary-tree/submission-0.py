# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def depthforsearch(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return depthforsearch(p.left, q.left) and depthforsearch(p.right, q.right)

        if not subRoot: # Edge case: subRoot is None (empty tree is always a subtree)
            return True
        if not root:   # Edge case: root is None but subRoot is not
            return False

        if depthforsearch(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)    