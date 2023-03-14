class Solution:
    stack = []
    nums = []
    index = 0
    def decodeString(self, s: str) -> str:
        if self.index >= len(s):
            res = "".join(self.stack)
            self.stack.clear()
            self.nums.clear()
            return res
        if s[self.index].isdigit():
            temp = []
            while s[self.index].isdigit():
                temp.append(s[self.index])
                self.index += 1
            self.nums.append(int("".join(temp)))
            return self.decodeString(s)

        elif s[self.index] == "]":
            temp = []
            answer = []
            while self.stack[len(self.stack)-1] != "[":
                temp.append(self.stack.pop())
            self.stack.pop()
            temp.reverse()
            temp = "".join(temp)
            for i in range(self.nums.pop()):
                answer.append(temp)
            self.stack.append("".join(answer))
        else:
            self.stack.append(s[self.index])
        self.index += 1  
        return self.decodeString(s)

                
