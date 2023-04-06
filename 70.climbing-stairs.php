/*
 * @lc app=leetcode id=70 lang=php
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function climbStairs($n) {
        $count = 0;
        
        while ($n > 0) {
            if ($n - 1 >= 0) {
                $count += 1;
                $n -= 1;
            }
            else if ($n - 2 >= 0) {
                $count += 2;
                $n -= 2;
            }
        }
        return $count;
    
    }
}
// @lc code=end

