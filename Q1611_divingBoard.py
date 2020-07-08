from typing import List

class Solution:
	def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
		# 跳板数k=0,输出空数组
		if k == 0:
			return []
		# 短板和长板的长度一致，只有一种方案
		elif shorter == longer:
			return [shorter * k]
		# 一般情况下，有k+1种可能性
		else:
			result = []
			for i in range(k+1):
				result += [shorter * (k - i) + longer * i]
			return result
