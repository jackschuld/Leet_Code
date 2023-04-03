#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cashRegister = []
        for bill in bills:
            if bill == 20:
                if 5 in cashRegister and 10 in cashRegister:
                    cashRegister.pop(cashRegister.index(5))
                    cashRegister.pop(cashRegister.index(10))
                elif cashRegister.count(5) > 2:
                    for pop in range(3):
                        cashRegister.pop(cashRegister.index(5))
                else:
                    return False
            elif bill == 10:
                if not 5 in cashRegister:
                    return False
                cashRegister.pop(cashRegister.index(5))
            cashRegister.append(bill)
        return True

        
# @lc code=end

