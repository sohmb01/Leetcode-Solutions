# Problem ID: 508
# Title: Most Frequent Subtree Sum
# Runtime: 4 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        mp = defaultdict(int)

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            mp[s]+=1
            return s
        
        dfs(root)
        highestFrequency = max(mp.values())
        res = []
        for s,val in mp.items():
            if val == highestFrequency:
                res.append(s)
        return res