class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        map = {}
        goodPairs=0
        for i in nums:
            if i in map: 
                goodPairs += map[i]
                map[i] += 1
            else:
                map[i] = 1
        return goodPairs
