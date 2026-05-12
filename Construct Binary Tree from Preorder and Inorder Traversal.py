# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # Ý tưởng:
        # preorder: [root | left subtree | right subtree]
        # inorder : [left subtree | root | right subtree]
        #
        # → phần tử đầu preorder luôn là root
        # → tìm root trong inorder để chia trái/phải

        # Map để tìm index nhanh O(1)
        inorder_index = {val: i for i, val in enumerate(inorder)}

        # Con trỏ duyệt preorder
        self.pre_idx = 0

        def build(left, right):
            # left, right là khoảng index trong inorder
            if left > right:
                return None

            # Lấy root từ preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            # Vị trí root trong inorder
            mid = inorder_index[root_val]

            # Xây cây trái trước (vì preorder đi root → left → right)
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)