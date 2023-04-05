/*
 * @lc app=leetcode id=58 lang=php
 *
 * [58] Length of Last Word
 */

// @lc code=start
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLastWord($s) {
        $words = array_filter(explode(" ", $s));
        return strlen(end($words));
    }
}
// @lc code=end

