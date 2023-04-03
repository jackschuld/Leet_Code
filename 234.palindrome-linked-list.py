#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        listList = []
        # Conver to list
        while head:
            listList.append(head.val)
            head = head.next
        # Pop out middle value on odds
        if len(listList) % 2 != 0:
            listList.pop(len(listList) // 2)
        return listList[:len(listList) // 2] == listList[len(listList) // 2:][::-1]
# @lc code=end

