import queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        '''
        :param root: TreeNode
        :return: List[int]
        time: O(N)
        space: O(N)
        '''
        q = queue.Queue()
        q.put([root, 0])
        result = []
        if not root: return result

        while (not q.empty()):
            tmp = q.get()
            if len(result) <= tmp[1]:
                result.append(tmp[0].val)
            else:
                result[tmp[1]] = tmp[0].val
            if tmp[0].left:
                q.put([tmp[0].left, tmp[1] + 1])
            if tmp[0].right:
                q.put([tmp[0].right, tmp[1] + 1])
        return result


'''
노드를 BFS 방식으로 방문. 
queue에 방문할 노드들을 입력하는데 (노드, 레벨) 함께 넣어줌. 
결과로 반환할 list를 result라고 하고, result의 인덱스 위치에는 각 레벨의 가장ㄴ 오른쪽 값이 저장되도록 함. 
(왼쪽부터 방문하면서 덮어쓰기를 하면 가장 오른쪽에 있는 노드의 값이 최종으로 저장됨) 
'''
