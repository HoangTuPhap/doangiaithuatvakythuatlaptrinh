# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1, root2):
        # Hàm lấy danh sách lá theo thứ tự trái → phải
        def get_leaves(node, leaves):
            if not node:
                return

            # Nếu là lá → thêm vào list
            if not node.left and not node.right:
                leaves.append(node.val)
                return

            # Duyệt trái rồi phải
            get_leaves(node.left, leaves)
            get_leaves(node.right, leaves)

        leaves1 = []
        leaves2 = []

        # Lấy danh sách lá của 2 cây
        get_leaves(root1, leaves1)
        get_leaves(root2, leaves2)

        # So sánh 2 list
        return leaves1 == leaves2