# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        # So sánh 2 cây có giống hệt nhau không
        def isSame(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False

            return isSame(a.left, b.left) and isSame(a.right, b.right)

        # Duyệt từng node trong root để tìm điểm bắt đầu
        def dfs(node):
            if not node:
                return False

            # Nếu match từ node hiện tại
            if isSame(node, subRoot):
                return True

            # Tìm tiếp ở trái hoặc phải
            return dfs(node.left) or dfs(node.right)

        return dfs(root)