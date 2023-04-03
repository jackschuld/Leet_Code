#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnLetters = ""
        length = (columnNumber / 26) + 1
        while len(columnLetters) != length :
            tempNum = (columnNumber % 26) - 1 
            columnLetters += chr(tempNum + 64)
            columnNumber -= 26
        return columnLetters

# @lc code=end

