class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        freq = Counter(s)

        for alpha in s:
            freq[alpha] -= 1
            if alpha in stack:
                continue
            while len(stack) != 0 and stack[len(stack)-1] > alpha and freq[stack[len(stack)-1]] > 0:
                stack.pop()
            stack.append(alpha)
 
        return "".join(stack)

        
