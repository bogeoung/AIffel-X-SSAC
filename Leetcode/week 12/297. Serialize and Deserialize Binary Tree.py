# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        list = []
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                list.append(str(node.val))
            else:
                list.append('n')
        return list


def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 아래 부분에서 빈 리스트를 잡지 못함
        # if not data: 로 빈 리스트가 입력이 되었을 때 잡으려고 했음.
        # 하지만 serialize를 거친 빈 리스트는 n이 추가되어서 desrialize를 호출하기 때문에
        # data[0] == 'n'으로 잡아야만 처음 serialize의 input이 빈 리스트인 것을 잡을 수 있음.
        if data[0] == 'n':
            return None

        root = TreeNode(data.pop(0))
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            temp = data.pop(0)
            if temp is not 'n':
                node.left = TreeNode(int(temp))
                queue.append(node.left)

            temp = data.pop(0)
            if temp is not 'n':
                node.right = TreeNode(int(temp))
                queue.append(node.right)
        return root




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

