# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root):
        # BFS dùng queue để duyệt theo từng level

        if not root:
            return []

        res = []
        q = deque([root])  # khởi tạo queue với root

        while q:
            level_size = len(q)  # số node trong level hiện tại
            level = []

            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)

                # thêm con vào queue cho level sau
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)  # lưu level hiện tại

        return res