# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        faster = head
        slower = head

        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next
            if faster == slower:
                return True
        return False
