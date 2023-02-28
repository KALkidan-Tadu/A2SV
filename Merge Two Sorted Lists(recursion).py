# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    merged = ListNode()
    temp1 = merged

    def merge(self,list1,list2):
        if list1 == None or list2 == None:
            while list1:
                self.temp1.next = ListNode(list1.val)
                self.temp1 = self.temp1.next
                list1 = list1.next
            while list2:
                self.temp1.next = ListNode(list2.val)
                self.temp1 = self.temp1.next
                list2 = list2.next 
            return self.merged.next
        if list1.val <= list2.val:
            self.temp1.next = ListNode(list1.val)
            self.temp1 = self.temp1.next
            list1 = list1.next
        else:
            self.temp1.next = ListNode(list2.val)
            self.temp1 = self.temp1.next
            list2 = list2.next
            
        return self.merge(list1, list2)
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.merged = ListNode()
        self.temp1 = self.merged
        return self.merge(list1,list2)

