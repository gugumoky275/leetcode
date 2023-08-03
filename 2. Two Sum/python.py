# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def invertList(self, l1: Optional[ListNode], acc: Optional[ListNode]=None) -> Optional[ListNode]:
        if l1:
            return self.invertList(l1.next, ListNode(l1.val, acc))
        return acc

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int=0) -> Optional[ListNode]:
        if not l1 and not l2:
            if carry:
                return ListNode(carry)
            return None
        
        if not l1:
            sum = l2.val + carry
            return ListNode(sum % 10, self.addTwoNumbers(l1, l2.next, sum // 10))
        
        if not l2:
            sum = l1.val + carry
            return ListNode(sum % 10, self.addTwoNumbers(l1.next, l2, sum // 10))
        
        sum = l1.val + l2.val + carry
        return ListNode(sum % 10, self.addTwoNumbers(l1.next, l2.next, sum // 10))

