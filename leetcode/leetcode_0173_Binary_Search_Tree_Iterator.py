# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator_1: #recursion
    def __init__(self, root: TreeNode):
        '''time: O(N)/ space: O(N)'''
        self.m = []
        self.idx = -1
        self.inorder(root)

    def inorder(self, node):
        if not node: return
        self.inorder(node.left)
        self.m.append(node.val)
        self.inorder(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        time: O(1)
        """
        self.idx += 1
        return self.m[self.idx]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        time: O(1)
        """
        return self.idx < len(self.m) - 1


class BSTIterator_2: #iteration
    def __init__(self, root: TreeNode):
        self.m = self.inorder(root)
        self.idx = -1

    def inorder(self, root):
        stack, res = [], []
        node = root
        while (stack or node):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.idx += 1
        return self.m[self.idx]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.idx < len(self.m) - 1


class BSTIterator_3: #iteration
    def __init__(self, root: TreeNode):
        self.stack = []  # space: O(h)
        self.node = root

    def next(self) -> int:
        """
        @return the next smallest number
        time: O(h)
        """
        while (self.stack or self.node):
            if self.node:
                self.stack.append(self.node)
                self.node = self.node.left
            else:
                self.node = self.stack.pop()
                res = self.node.val
                self.node = self.node.right
                return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        time: O(1)
        """
        return self.stack or self.node

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()