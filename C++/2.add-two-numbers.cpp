/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
 */

// @lc code=start
// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}

//  };
#include <iostream>
struct ListNode;

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        int sum = 0;
        ListNode *l3 = malloc(sizeof(struct ListNode));
        l4 = l3;

        while (l1 || l2) {
            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }

            l3->val = sum % 10;
            sum /= 10;
            l3 = l3->next;

            std::cout << l1->val << " " << l2->val << " " << l3->val << " " << sum << "\n";
        }

        return l3;

    }
};
// @lc code=end

