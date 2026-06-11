# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hm = {}
        idx = 0
        while head != None:
            if head in hm:
                return True
            else:
                hm[head] = idx
            idx += 1
            head = head.next
        return False