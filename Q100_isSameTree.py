# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
		# 使用同样的方式遍历两棵树，如果每个节点具有相同的值则返回True，否则返回False
		if p is None or q is None:
			return p == q
		elif p.left is None and p.right is None:
			return p.val == q.val
		else:
			if p.val == q.val:
				return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
			else:
				return False
