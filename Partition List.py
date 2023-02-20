# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater = ListNode()
        lessthan = ListNode()
        temp1 = lessthan
        temp2 = greater
        curr = head
        while curr:
            if curr.val < x:
                temp1.next = ListNode(curr.val)
                temp1 = temp1.next
            else:
                temp2.next = ListNode(curr.val)
                temp2 = temp2.next
            curr = curr.next
        temp1.next = greater.next
        return lessthan.next
