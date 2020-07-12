from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0]

    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        for index in range(i, j+1):
            sum += self.nums[index]
        return sum

    def sumRange_v2(self, i: int, j:int) -> int:
        for index in range(len(self.nums)):
            self.sums.append(self.nums[index] + self.sums[len(self.sums)-1])
        return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

nums = [-2, 0, 3, -5]
i = 0
j = 1
myNumArray = NumArray(nums)
myNumArray.sumRange_v2(i, j)