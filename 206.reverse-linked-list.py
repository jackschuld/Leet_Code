#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        currentNode = head
        while currentNode:
            next = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = next
        return prevNode
            
        
        
# @lc code=end

