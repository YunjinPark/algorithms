#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        :param root: TreeNode
        :return: bool
        time: O(N)
        space: O(N)
        '''
        if not root: return True

        lNode = root.left
        rNode = root.right

        lQ = queue.Queue()
        rQ = queue.Queue()

        if not lNode and not rNode:
            return True
        elif (lNode and rNode) and (lNode.val == rNode.val):
            lQ.put(lNode)
            rQ.put(rNode)
        else:
            return False

        while (not lQ.empty()) and (not rQ.empty()):
            lNode = lQ.get()
            rNode = rQ.get()

            if not lNode.left and not rNode.right:
                pass
            elif (lNode.left and rNode.right) and (lNode.left.val == rNode.right.val):
                lQ.put(lNode.left)
                rQ.put(rNode.right)
            else:
                return False

            if not lNode.right and not rNode.left:
                pass
            elif (lNode.right and rNode.left) and (lNode.right.val == rNode.left.val):
                lQ.put(lNode.right)
                rQ.put(rNode.left)
            else:
                return False

        if (not lQ) or (not rQ): return False

        return True


'''
isSymmetric
왼쪽 서브트리와 오른쪽 서브트리를 비교.
노드 방문은 BFS로 함. 
왼쪽 서브트리는 왼쪽에서부터 노드를 방문했다면 오른쪽 서브트리는 오른쪽에서부터 노드를 방문하면서 노드의 값이 같은지 비교. 
'''