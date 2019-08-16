# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        :param root: TreeNode
        :return:  bool
        time: O(N)
        space: O(N)
        '''
        stack = []
        if root: stack.append([root, float('-Inf'), float('Inf')])
        while (stack):
            node, lower, upper = stack.pop()
            if node.val >= upper or node.val <= lower: return False
            if node.left: stack.append([node.left, lower, node.val])
            if node.right: stack.append([node.right, node.val, upper])
        return True

'''
BFS 방법으로 노드 방문 
상한, 하한을 만족하지 않을 경우 False
left 자식의 조건: 부모의 하한은 그대로, 상한은 부모의 value 
right 자식의 조건: 하한은 부모의 value, 상한은 부모의 상한 그대로  
'''
