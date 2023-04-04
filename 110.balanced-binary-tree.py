#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        def checkHeight(root):
            if root == None:
                return 0
            return 1 + max(checkHeight(root.left), checkHeight(root.right))
        
        comp = abs(checkHeight(root.left) - checkHeight(root.right))
        if comp > 1:
            return False
        
        leftside = self.isBalanced(root.left)
        rightside = self.isBalanced(root.right)

        if leftside and rightside:
            return True
        return False

            

            
        
        

# @lc code=end

