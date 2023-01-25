class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
    
        chemistry = 0
        left = 0
        right = len(skill)-1
        sum = skill[left] + skill[right]

        while left<right:
            if skill[left] + skill[right] != sum:
                return -1
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1

        return chemistry
