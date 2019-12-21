# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.a = 1

        def depth(node: TreeNode):
            if node: return 0
            l = depth(node.left)
            r = depth(node.right)
            self.a = max(self.a, l + r + 1)
            return max(l, r) + 1

        depth(root)
        depth(root)
        return self.a - 1