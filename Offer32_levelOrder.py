from typing import List
from collections import deque

# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        node_deque = deque()
        node_deque.append(root)
        while root.left or root.right:
            node_deque.append([root.left, root.right])
        return


# TODO: 使用广度优先搜索BFS解题
