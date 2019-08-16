from collections import deque
import queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        '''
        :param root: TreeNode
        :return: List[List[int]]
        time: O(N)
        space: O(N)
        '''

        q = queue.Queue()
        if root: q.put([root, 0])
        result = []
        while not q.empty():
            node, level = q.get()

            if len(result) <= level:
                tmp = deque()
                tmp.append(node.val)
                result.append(tmp)
            else:
                if level % 2 == 0:
                    result[level].append(node.val)
                else:
                    result[level].appendleft(node.val)
            if node.left: q.put([node.left, level+1])
            if node.right: q.put([node.right, level+1])

        return result

'''
노드를 BFS 방식으로 방문함. (queue 사용)
노드를 홀수 레벨에서나 짝수 레벨에서나 왼쪽부터 방문하지만, 값을 저장할 때는 홀수 레벨은 오른쪽부터, 짝수 레벨은 왼쪽부터임.  
각 레벨의 값을 저장할 때는 deque를 사용(doubly ended queue) 
홀수 레벨에서는 appendleft로 입력
짝수 레벨에서는 append로 입력
'''