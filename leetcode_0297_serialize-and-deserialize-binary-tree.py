import queue


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        time: O(N)
        space: O(N)
        """
        r = []
        q = queue.Queue()

        if root:
            q.put(root)
        print()
        while not q.empty():
            tmp = q.get()
            if tmp:
                r.append(str(tmp.val))
                q.put(tmp.left)
                q.put(tmp.right)
            else:
                r.append('null')

        while r and r[-1] == "null":
            del r[-1]

        return ','.join(r)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        time: O(N)
        space: O(N)
        """
        if not data: return None
        data = data.split(',')

        if data[0] != 'null':
            head = TreeNode(int(data[0]))
        else:
            return None
        q = queue.Queue()
        q.put(head)

        i = 0
        while q:
            tmp = q.get()
            if (i+1 < len(data)) and (data[i+1] != 'null'):
                tmp.left = TreeNode(int(data[i+1]))
                q.put(tmp.left)
            if (i+2 < len(data)) and (data[i+2] != 'null'):
                tmp.right = TreeNode(int(data[i+2]))
                q.put(tmp.right)
            i = i + 2
            if i > len(data):
                break

        return head

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

