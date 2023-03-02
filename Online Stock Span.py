class StockSpanner:
    nums = []
    mono = []
    d = {}
    def __init__(self):
        self.nums = self.nums
        self.mono = []
        self.d = {}

    def next(self, price: int) -> int:
        self.nums.append(price)
        counter = 1
        index = len(self.nums)-1
        while len(self.mono) != 0 and self.nums[self.mono[-1]] <= self.nums[index]:
            n = self.mono.pop()
            counter += self.d[n]
        self.d[index] = counter
        self.mono.append(index)
        return counter


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
