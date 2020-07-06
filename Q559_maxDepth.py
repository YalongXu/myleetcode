from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def maxDepth(self, root: Node) -> int:
        if root is None:
            return 0

        max_depth = 1
        node_dq = deque()
        node_dq += root.children

        while node_dq:
            max_depth += 1
            dq_length = len(node_dq)
            while dq_length > 0:
                dq_length -= 1
                node = node_dq.popleft()
                if node.children:
                    node_dq += node.children
        return max_depth

    def maxDepth_v2(self, root: Node) -> int:
        # 基线条件
        if root is None:
            return 0
        elif root.children is None:
            return 1
        else:
            # 递归条件
            height = [self.maxDepth_v2(node) for node in root.children]
            return max(height) + 1


#################
Node11 = Node(5)
Node12 = Node(6)
Node21 = Node(3, [Node11, Node12])
Node22 = Node(2)
Node23 = Node(4)
Node31 = Node(1, [Node21, Node22, Node23])

mySolution = Solution()
calcDepth = mySolution.maxDepth(Node31)
print(calcDepth)
print(mySolution.maxDepth_v2(Node31))