/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
#include <vector>
#include <iostream>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (i != j) {
                    int sum = nums[i] + nums[j];
                    if (sum == target) {
                        std::vector<int> output = {i, j};
                        return output;
                    }
                }
            }
        }
        return nums;
    }
};
// @lc code=end

