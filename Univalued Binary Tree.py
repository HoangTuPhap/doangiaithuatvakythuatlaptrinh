# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root):
        # Lưu giá trị chuẩn (giá trị của root)
        target = root.val

        def dfs(node):
            # Nếu node rỗng → hợp lệ
            if not node:
                return True

            # Nếu khác giá trị chuẩn → không phải uni-valued
            if node.val != target:
                return False

            # Kiểm tra tiếp 2 nhánh
            return dfs(node.left) and dfs(node.right)

        return dfs(root)