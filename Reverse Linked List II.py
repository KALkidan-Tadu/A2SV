# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        index = 1
        curr = head
        nodes = []
        while index < left:
            curr = curr.next
            index += 1
        start = curr
        while index <= right:
            nodes.append(curr.val)
            curr = curr.next
            index += 1
        nodes.reverse()
        for node in nodes:
            start.val = node
            start = start.next
        
        return head



