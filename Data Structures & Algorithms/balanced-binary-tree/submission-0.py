# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(root):
            if not root:
                return [0, True]

            left = get_height(root.left)
            right = get_height(root.right)

            left_height = left[0]
            right_height = right[0]
            left_balanced = left[1]
            right_balanced = right[1]

            if not left_balanced or not right_balanced or abs(left_height - right_height) > 1:
               return [0, False]

            else:
               return [1 + max(left_height, right_height), True]
            
        return get_height(root)[1]