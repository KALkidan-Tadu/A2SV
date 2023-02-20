# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        if size-n == 0:
            head = head.next
            
        temp = head
        for index in range(size-n-1):
            temp = temp.next
        
        if temp and temp.next:
            temp.next = temp.next.next
        return head
