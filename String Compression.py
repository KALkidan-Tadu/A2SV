class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 1

        while right < len(chars):
            count = 1
            while right < len(chars) and chars[left] == chars[right]:
                count += 1
                right += 1

            if count == 1:
                left = right
                right += 1

            else:
                right -= 1
                while right > left:
                    chars.pop(right)
                    right -= 1
                rep = str(count)
                index = left + 1
                for c in rep:
                    chars.insert(index, c)
                    index += 1
                left = index 
                right = left + 1
                
        return len(chars)

        
        
