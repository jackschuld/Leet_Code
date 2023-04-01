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
        def results(root):

            if root is None:
                return [True, 0]
            leftheight, rightheight = results(root.left), results(root.right)
            print(leftheight, rightheight)
            check = (leftheight[0] and rightheight[0] and abs(leftheight[1]-rightheight[1] <= 1))
            print(check)
            return [check, 1 + max(leftheight[1], rightheight[1])]
        return results(root)[0]
        
        
        

# @lc code=end

