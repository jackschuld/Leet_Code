/*
 * @lc app=leetcode id=13 lang=cpp
 *
 * [13] Roman to Integer
 */

// @lc code=start
#include <iostream>

class Solution {
public:
    int addInt(char t) {
        if (t == 'I') {
            return 1;
        }
        else if (t == 'V') {
            return 5;
        }
        else if (t == 'X') {
            return 10;
        }
        else if (t == 'L') {
            return 50;
        }
        else if (t == 'C') {
            return 100;
        }
        else if (t == 'D') {
            return 500;
        }
        else if (t == 'M') {
            return 1000;
        }
        return 0;
    }

    int romanToInt(std::string s) {
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            // Check if potential subtraction case
            if (s[i + 1]){
                if (s[i] == 'I' && s[i + 1] == 'V') {
                    sum += 4;
                    i++;
                }
                else if (s[i] == 'I' && s[i + 1] == 'X') {
                    sum += 9;
                    i++;
                }
                else if (s[i] == 'X' && s[i + 1] == 'L') {
                    sum += 40;
                    i++;
                }
                else if (s[i] == 'X' && s[i + 1] == 'C') {
                    sum += 90;
                    i++;
                }
                else if (s[i] == 'C' && s[i + 1] == 'D') {
                    sum += 400;
                    i++;
                }
                else if (s[i] == 'C' && s[i + 1] == 'M') {
                    sum += 900;
                    i++;
                }
                else {
                    sum += addInt(s[i]);
                }
            }
            else {
                sum += addInt(s[i]);
            }
        }
        return sum;
    }
};
// @lc code=end

