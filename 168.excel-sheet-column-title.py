#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnLetters = ""
        while columnNumber > 0:
            columnNumber -= 1
            columnLetters += chr((columnNumber % 26) + 65)
            columnNumber //= 26
        return columnLetters[::-1]
    
# @lc code=end

