# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        counter = head
        while counter != None:
            length += 1
            counter = counter.next
        idx = length - n

        if length - n == 0:
            return head.next
        
        temp = head
        prev = head
        while idx > 0:
            prev = temp
            temp = temp.next
            idx -= 1
        prev.next = temp.next
        return head
        