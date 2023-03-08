class Solution:
    def count(self, s):
        s = sorted(s)
        c = 0
        for w in s:
            if w != s[0]:
                break
            c += 1
        return c

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        nums = []
        for word in words:
            nums.append(self.count(word))
        
        nums.sort()
        answer = []

        for q in queries:
            target = self.count(q)
            index = bisect_left(nums, target)
            if index >= len(nums):
                answer.append(0)
            else:
                if nums[index] == target:
                    while index < len(nums) and nums[index] == target:
                        index += 1
                if index >= len(nums):
                    answer.append(0)
                else:
                    answer.append(len(nums) - index)
        
        return answer
