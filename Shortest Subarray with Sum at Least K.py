class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        mono = deque()
        shortest = len(nums)+1
        prefix = [0]*(len(nums)+1)

        for i in range(1,len(prefix)):
            prefix[i] = prefix[i-1] + nums[i-1]

        for right in range(len(prefix)):
            while len(mono)!=0 and prefix[right] - prefix[mono[0]] >= k:
                shortest = min(shortest, right-mono.popleft())     
            while len(mono) != 0 and prefix[mono[-1]] > prefix[right]:
                mono.pop()
            mono.append(right)
        if shortest == len(nums)+1:
            return -1
        return shortest
