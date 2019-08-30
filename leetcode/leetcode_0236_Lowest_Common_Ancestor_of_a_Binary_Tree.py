# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        '''
        :param root: 'TreeNode'
        :param p: 'TreeNode'
        :param q: 'TreeNode'
        :return: 'TreeNode'
        time:
        space:
        '''

        def preOrder(node, level):
            '''
            :param node:
            :return: None
            '''
            nonlocal tmp
            nonlocal pList, qList
            if not node:
                return None
            else:
                if len(tmp) <= level:
                    tmp.append(node)
                else:
                    tmp[level] = node
                if node == p:
                    pList = tmp[:level + 1]
                if node == q:
                    qList = tmp[:level + 1]
                if pList and qList: return None
                preOrder(node.left, level + 1)
                preOrder(node.right, level + 1)

        tmp, pList, qList = [], [], []

        preOrder(root, 0)

        result = None

        for i in range(0, min(len(pList), len(qList))):
            if pList[i] == qList[i]:
                result = pList[i]
            else:
                break
        return result

'''
dfs 방법으로 노드 p와 q를 찾는다.
노드를 검색할 때 조상 노드들을 누적해서 저장해둔다. 
p와 q를 찾으면 p와 q 각각의 조상노드들을 알 수 있다.
조상 노드들을 차례대로 비교해가면서 가장 낮은 차원의 공통된 조상을 반환한다. 
'''