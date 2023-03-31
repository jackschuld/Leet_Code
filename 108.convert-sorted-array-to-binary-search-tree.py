#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total = len(nums)

        if total:
            mid_node = total//2
            return TreeNode(nums[mid_node], self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1:]))
        return None

        
# @lc code=end

