# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        size = 0
        temp = head
        while temp:
            temp = temp.next
            size += 1

        curr = head
        for i in range(size//2):
            curr = curr.next
        nodes = []
        temp = curr
        half = curr
        while temp:
            nodes.append(temp.val)
            temp = temp.next
        nodes.reverse()
        for node in nodes:
            curr.val = node
            curr = curr.next
        maxsum = 0
        left = head
        while half:
            maxsum = max(maxsum, left.val+half.val)
            left = left.next
            half = half.next
        return maxsum
