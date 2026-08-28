# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # global tracker for length
        res = 0

        # recursive function
        def dfs(curr):
            if not curr:
                return 0
            # heights of each sub tree
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            # return the legth including the current node
            nonlocal res
            res = max(res, left + right)

            return max(left, right) + 1

        dfs(root)
        return res
