from collections import deque

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def hasPathSum(self, root: TreeNode, sum: int) -> bool:
		if root is None:
			return False
		dq_node = deque([root])
		dq_path_sum = deque([root.val])
		while dq_node:
			node = dq_node.popleft()
			path_sum = dq_path_sum.popleft()
			if path_sum == sum and node.left is None and node.right is None:
				return True
			else:
				if node.left:
					dq_node.append(node.left)
					dq_path_sum.append(path_sum + node.left.val)
				if node.right:
					dq_node.append(node.right)
					dq_path_sum.append(path_sum + node.right.val)
		return False


root = TreeNode(5)
root.left = TreeNode(4)
sum = 9
mySolution = Solution()
result = mySolution.hasPathSum(root, sum)
print(result)


'''
方法二：递归
思路及算法
观察要求我们完成的函数，我们可以归纳出它的功能：询问是否存在从当前节点root到叶子节点的路径，满足其路径和为sum。
假定从根节点到当前节点的值之和为 val，我们可以将这个大问题转化为一个小问题：
是否存在从当前节点的子节点到叶子的路径，满足其路径和为 sum - val。
不难发现这满足递归的性质，若当前节点就是叶子节点，那么我们直接判断 sum 是否等于 val 即可,因为路径和已经确定，就是当前节点的值，我们只需要判断该路径和是否满足条件;
若当前节点不是叶子节点，我们只需要递归地询问它的子节点是否能满足条件即可。
'''
def has_path_sum(root: TreeNode, sum: int) -> bool:
	if root is None:
		return False
	else:
		if root.left is None and root.right is None:
			return root.val == sum
		return has_path_sum(root.left, sum - root.val) or has_path_sum(root.right, sum - root.val)


result = has_path_sum(root, sum)
print(result)

