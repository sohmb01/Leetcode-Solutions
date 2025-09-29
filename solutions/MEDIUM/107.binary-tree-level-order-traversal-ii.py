# Problem ID: 107
# Title: Binary Tree Level Order Traversal II
# Runtime: 32 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans=[]
        if not root :
            return 
        else:
            
            q=[]
            q.append(root)
            while(len(q)>0):
                h=[]
                k=len(q)
                for i in range(k):
                    temp=q.pop(0)
                    h.append(temp.val)
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                ans.append(h)
            return ans[::-1]
                    
                    
            
        