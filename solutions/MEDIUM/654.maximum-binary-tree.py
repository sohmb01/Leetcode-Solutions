# Problem ID: 654
# Title: Maximum Binary Tree
# Runtime: 35 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        
        idx = -1
        mx = -float('inf')
        for i,num in enumerate(nums):
            if num>mx:
                idx = i
                mx = num
        node = TreeNode()
        node.val = mx
        node.left = self.constructMaximumBinaryTree(nums[:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return node
