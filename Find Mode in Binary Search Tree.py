# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root):
        # Inorder của BST → dãy không giảm → dễ đếm liên tiếp (tối ưu O(1) extra space, bỏ stack)
        
        self.prev = None   # giá trị trước đó
        self.count = 0     # số lần xuất hiện hiện tại
        self.maxCount = 0  # tần suất lớn nhất
        self.res = []      # danh sách mode

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            # Nếu giống giá trị trước → tăng count, ngược lại reset
            if self.prev == node.val:
                self.count += 1
            else:
                self.count = 1

            # Cập nhật prev
            self.prev = node.val

            # Nếu đạt max → thêm vào kết quả
            if self.count == self.maxCount:
                self.res.append(node.val)

            # Nếu vượt max → reset danh sách
            elif self.count > self.maxCount:
                self.maxCount = self.count
                self.res = [node.val]

            inorder(node.right)

        inorder(root)
        return self.res