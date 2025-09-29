# Problem ID: 108
# Title: Convert Sorted Array to Binary Search Tree
# Runtime: 56 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        node = TreeNode()
        node.val=nums[len(nums)//2]
        node.left=self.sortedArrayToBST(nums[:len(nums)//2])
        node.right=self.sortedArrayToBST(nums[len(nums)//2+1:])
        return node