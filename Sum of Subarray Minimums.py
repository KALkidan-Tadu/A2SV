class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = pow(10, 9) + 7
        stack = []
        answer = [0]*(len(arr))
        sum = 0

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                answer[i] = answer[stack[-1]] + arr[i] * (i- stack[-1])
            else:
                answer[i] = arr[i]* (i+1)
            stack.append(i)
            sum += answer[i]
        return int(sum % mod)
            

    

