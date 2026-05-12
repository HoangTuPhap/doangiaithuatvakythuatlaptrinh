# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root):
        # DFS: left → root → right

        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)        # duyệt trái
            res.append(node.val)  # thêm root
            dfs(node.right)       # duyệt phải

        dfs(root)
        return res