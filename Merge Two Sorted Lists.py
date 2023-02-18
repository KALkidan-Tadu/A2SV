# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        temp1 = merged

        while list1 and list2:
            if list1.val <= list2.val:
                temp2 = ListNode(list1.val)
                temp1.next = temp2
                temp1 = temp2
                list1 = list1.next
            else:
                temp2 = ListNode(list2.val)
                temp1.next = temp2
                temp1 = temp2
                list2 = list2.next
        
        while list1:
            temp2 = ListNode(list1.val)
            temp1.next = temp2
            temp1 = temp2
            list1 = list1.next

        while list2:
            temp2 = ListNode(list2.val)
            temp1.next = temp2
            temp1 = temp2
            list2 = list2.next
        
        return merged.next
