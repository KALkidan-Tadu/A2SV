# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        n1 = l1
        n2 = l2
        while n1:
            num1.append(str(n1.val))
            n1 = n1.next
        while n2:
            num2.append(str(n2.val))
            n2 = n2.next
        num1.reverse()
        num2.reverse()
        num1 = int("".join(num1))
        num2 = int("".join(num2))
        num3 = list(map(int, str(num1+num2)))
        num3.reverse()
        newNode = ListNode()
        start = newNode
        for i in range(len(num3)):
            start.next = ListNode(num3[i])
            start = start.next
        return newNode.next
