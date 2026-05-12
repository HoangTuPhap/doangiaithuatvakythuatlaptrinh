# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        # Chọn middle làm root → đảm bảo cân bằng
        # left part → subtree trái
        # right part → subtree phải

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2  # chọn middle
            root = TreeNode(nums[mid])

            # xây 2 nhánh
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)