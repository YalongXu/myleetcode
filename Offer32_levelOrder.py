from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        dq = deque()
        dq.append(root)
        result_list = []
        while dq:
            dq_length = len(dq)
            tmp_list = []
            while dq_length > 0:
                dq_length -= 1
                node = dq.popleft()
                if node is not None:
                    tmp_list += [node.val]
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
            result_list.append(tmp_list)
        return result_list


# TODO: 使用广度优先搜索BFS解题
