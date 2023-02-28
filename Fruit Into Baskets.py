class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        maxfruit = 0
        unique = defaultdict(int)
        count = 0

        for right in range(len(fruits)):
            if fruits[right] not in unique or unique[fruits[right]]==0:
                count += 1
            unique[fruits[right]] += 1
            while count > 2:
                unique[fruits[left]] -= 1
                if unique[fruits[left]] == 0:
                    count -= 1
                left += 1
            maxfruit = max(maxfruit, right - left + 1)
        
        return maxfruit
                 
