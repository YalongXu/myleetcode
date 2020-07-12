from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        动态规划寻找最大子序列和
        :param nums: List[int]
        :return: max sum of sub array
        '''
        if nums is None:
            maxVal = 0
        else:
            # maxVal保存最大子序列和
            maxVal = nums[0]
            # dp[1], dp[0]保存最近两次最大子序列和
            # if dp[i-1] > 0, dp[i] = dp[i-1] + nums[i]
            # if dp[i-1] <= 0, dp[i] = nums[i]
            dp = [nums[0], nums[0]]
            for index in range(1, len(nums)):
                if dp[0] > 0:
                    dp[1] = nums[index] + dp[0]
                else:
                    dp[1] = nums[index]
                dp[0] = dp[1]
                maxVal = max(maxVal, dp[1])
        return maxVal

    def maxSubArray_v2(self, nums: List[int]) -> int:

        def maxSub(nums: List[int], left: int, right: int) -> int:
            maxLeftBorderSum = maxRightBorderSum = float('-inf')
            leftMaxSum = rightMaxSum = float('-inf')
            leftBorderSum = rightBorderSum = 0

            mid = left + (right - left) // 2
            if left == right:
                return nums[left]
            leftMaxSum = maxSub(nums, left, mid)
            rightMaxSum = maxSub(nums, mid+1, right)

            for i in range(mid, left-1, -1):
                leftBorderSum += nums[i]
                if leftBorderSum > maxLeftBorderSum:
                    maxLeftBorderSum = leftBorderSum

            for i in range(mid+1, right+1, 1):
                rightBorderSum += nums[i]
                if rightBorderSum > maxRightBorderSum:
                    maxRightBorderSum = rightBorderSum

            return max(leftMaxSum, rightMaxSum, maxLeftBorderSum+maxRightBorderSum)

        return maxSub(nums, 0, len(nums)-1)

nums = [-2,1,-3,4,-1,2,1,-5,4]
mySolution = Solution()
maxVal = mySolution.maxSubArray(nums)
print(maxVal)
maxVal1 = mySolution.maxSubArray_v2(nums)
print(maxVal1)