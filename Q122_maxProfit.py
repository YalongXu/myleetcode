from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		if prices is None:
			return 0
		buy = sell = earn = 0
		stock = False
		cur = float("inf")
		for i in range(len(prices)):
			nxt = prices[i]
			if cur < nxt and not stock:
				stock = True
				buy = cur
			elif stock:
				if cur > nxt and stock:
					stock = False
					sell = cur
					earn += sell - buy
			cur = nxt
		if stock:
			sell = nxt
			earn += sell - buy
		return earn

	def maxProfit_v2(self, prices: List[int]) -> int:
		max_profit = 0
		i = 1
		for i in range(1, len(prices)):
			if prices[i-1] < prices[i]:
				max_profit += prices[i] - prices[i-1]
		return max_profit


prices = [7, 1, 5, 3, 6, 4]
mySolution = Solution()
print(mySolution.maxProfit(prices))
print(mySolution.maxProfit_v2(prices))



