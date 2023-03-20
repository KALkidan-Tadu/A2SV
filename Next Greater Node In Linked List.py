# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        stack = []

        while head:
            nums.append(head.val)
            head = head.next
        answer = [0] * len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                answer[stack.pop()] = nums[i]
            stack.append(i)
        
        return answer
