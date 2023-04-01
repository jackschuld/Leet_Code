#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largestReturn = 0
        for i in range(len(prices)):
            for j in prices[i:]:
                if j - prices[i] > largestReturn:
                    print("Larger Return:\n")
                    print(j)
                    print(prices[i])
                    largestReturn = j - prices[i]
        if largestReturn > 0:
            return largestReturn
        return 0
        
# @lc code=end

