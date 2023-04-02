#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapestPrice = float("inf")
        maxReturnProfit = 0
        for price in prices:
            if price > cheapestPrice:
                if price - cheapestPrice > maxReturnProfit:
                    maxReturnProfit = price - cheapestPrice
            else:
                cheapestPrice = price
        return maxReturnProfit
        
# @lc code=end

