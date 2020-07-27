class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		if len(s) == 0:
			return True
		index_s = 0
		index_t = 0
		for t_ch in t:
			if index_s == len(s):
				break
			elif t_ch == s[index_s]:
				index_s += 1
			index_t += 1
		if index_s == len(s):
			return True
		else:
			return False

	def isSubsequence_v2(self, s: str, t: str) -> bool:
		n, m = len(s), len(t)
		f = [[0]*26 for _ in range(m)]
		f.append([m]*26)

		for i in range(m - 1, -1, -1):
			for j in range(26):
				f[i][j] = i if ord(t[i]) == j + ord('a') else f[i+1][j]

		add = 0
		for i in range(n):
			if f[add][ord(s[i]) - ord('a')] == m:
				return False
			add = f[add][ord(s[i]) - ord('a')] + 1
		return True


s = "abc"
t = "dddabdacdfd"
mySolution = Solution()
if mySolution.isSubsequence(s, t):
	print("Y")
else:
	print("N")

if mySolution.isSubsequence_v2(s, t):
	print("Y")
else:
	print("N")

