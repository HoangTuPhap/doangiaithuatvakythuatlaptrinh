# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root):
        # DFS: left → right → root

        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)    # duyệt trái
            dfs(node.right)   # duyệt phải
            res.append(node.val)  # thêm root sau cùng

        dfs(root)
        return res