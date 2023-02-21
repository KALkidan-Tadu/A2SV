# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k==0:
            return head
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1
        k = k%size
        if k == 0:
            return head
        curr = head
        for index in range(size-k):
            if index == size-k-1:
                n = curr
                curr = curr.next
                n.next = None
            else:
                curr = curr.next
        start = ListNode()
        start.next = curr
        while curr.next != None:
            curr = curr.next
        curr.next = head

        return start.next

