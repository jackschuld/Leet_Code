#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, num1 in enumerate(nums):
            for i2, num2 in enumerate(nums):
                if i1 != i2 and num1 + num2 == target:
                    return [i1, i2]

# @lc code=end

