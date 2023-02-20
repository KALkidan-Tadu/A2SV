# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # faster = head
        # slower = head
        
        # while faster and faster.next:
        #     slower = slower.next
        #     faster = faster.next.next
        #     if slower == faster:
        #         break
        
        # if faster == None or faster.next == None:
        #     return None
        
        # slower =head
        # while slower != faster:
        #     slower = slower.next
        #     faster = faster.next
        # return slower

        curr = head
        nodes = set()

        while curr:
            if curr in nodes:
                return curr
            nodes.add(curr)
            curr = curr.next
        return None
