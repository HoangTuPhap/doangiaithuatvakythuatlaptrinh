# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root):
        # DFS: hoán đổi left và right cho từng node

        if not root:
            return None

        # Đảo 2 nhánh
        root.left, root.right = root.right, root.left

        # Đệ quy xuống dưới
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root