#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = [f"{root.val}"]
        tempRoot = root
        currPath = 0
        while tempRoot.left:
            paths[currPath] += f"->{tempRoot.left.val}"
            tempRoot = tempRoot.left
        while tempRoot.right:
            paths[currPath] += f"->{tempRoot.right.val}"
            tempRoot = tempRoot.right
        currPath += 1
        tempRoot = root
        if tempRoot.right or tempRoot.left:
            paths += f"{tempRoot.val}"
        while tempRoot.right:
            paths[currPath] += f"->{tempRoot.right.val}"
            tempRoot = tempRoot.right
        while tempRoot.left:
            paths[currPath] += f"->{tempRoot.left.val}"
            tempRoot = tempRoot.left
        return [*set(paths)]

# @lc code=end

