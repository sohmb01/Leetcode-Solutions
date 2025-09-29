# Problem ID: 113
# Title: Path Sum II
# Runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(curr, target, l, ans):
            if not curr:
                return 
            l.append(curr.val)
            if curr.val == target and not (curr.left or curr.right):
                ans.append(list(l))

            dfs(curr.left,target-curr.val,l,ans)
            dfs(curr.right,target-curr.val,l,ans)
            l.pop()
        
        ans = []
        dfs(root,targetSum,[],ans)
        return ans