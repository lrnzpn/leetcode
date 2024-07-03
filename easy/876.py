"""
https://leetcode.com/problems/middle-of-the-linked-list/
"""
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first implem, using a helper function to convert list to linkedlist
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def list_to_link(lst):
            if len(lst) == 1:
                return ListNode(lst[0])
            return ListNode(lst[0], list_to_link(lst[1:]))  
        size = 0
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
            size+=1
        return list_to_link(arr[size // 2:])
    
# second implem, using pointers
class Solution:
    # optimal, slow pointer points to middle node while fast pointer goes ahead
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow