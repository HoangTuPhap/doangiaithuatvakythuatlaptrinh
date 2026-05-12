# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        # Dùng giới hạn min/max cho mỗi node
        # node phải nằm trong khoảng (low, high)

        def dfs(node, low, high):
            if not node:
                return True

            # Nếu vi phạm điều kiện BST
            if not (low < node.val < high):
                return False

            # Trái: cập nhật high = node.val
            # Phải: cập nhật low = node.val
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float('inf'))