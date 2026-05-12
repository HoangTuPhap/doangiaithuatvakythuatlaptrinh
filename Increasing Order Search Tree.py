# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root):
        # Tránh dùng nonlocal → dùng biến instance (self.cur)

        self.dummy = TreeNode(0)  # node giả
        self.cur = self.dummy     # con trỏ hiện tại

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            # xử lý node hiện tại
            node.left = None
            self.cur.right = node
            self.cur = node

            inorder(node.right)

        inorder(root)
        return self.dummy.right