# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # 큐 생성 후 root를 원소로 넣음.
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth +=1
            # 부모노드의 길이만큼 반복함.
            for _ in range(len(queue)):
                # queue.popright()를 넣어보니 존재하지 않는 메소드라고 떴음.
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)

        return depth
#
# def maxDepth(slef, root:TreeNode) -> int:
#     BFS는 큐를 사용하기 때문에 큐 선언. (DFS는 스택 사용)
#     queue = collections.deque([root])
#     depth = 0
#
#     while queue:
#
#     return depth