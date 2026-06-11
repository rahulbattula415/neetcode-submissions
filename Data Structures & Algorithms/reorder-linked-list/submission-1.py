# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1 - Get second half of linked list - requires length
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Step 2 - Reverse Second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Step 3 - Merge
        firstHalf = head
        secondHalf = prev
        while secondHalf:
            firstNext = firstHalf.next
            secondNext = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = firstNext
            firstHalf = firstNext
            secondHalf = secondNext

