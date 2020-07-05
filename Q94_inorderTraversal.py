from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderPrint(self, root: TreeNode):
        self.root = []
        def iterate_treenode(node: TreeNode):
            if node is None:
                return
            iterate_treenode(node.left)
            print(node.val)
            iterate_treenode(node.right)
            return

        iterate_treenode(root)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 保存中序遍历产生的List
        self.root = []

        # 中序遍历，每次迭代都将节点添加到列表中
        def iterate_treenode(node: TreeNode):
            if node is None:
                return
            iterate_treenode(node.left)
            self.root.append(node.val)
            iterate_treenode(node.right)
            return

        # 调用中序遍历子程序
        iterate_treenode(root)
        # 返回结果
        return self.root

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

mySolution = Solution()
mySolution.inorderPrint(root)
resultList = mySolution.inorderTraversal(root)


for n in resultList:
    print(n, end=' ')




