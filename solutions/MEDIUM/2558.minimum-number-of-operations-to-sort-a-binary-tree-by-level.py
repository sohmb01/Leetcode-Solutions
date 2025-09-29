# Problem ID: 2558
# Title: Minimum Number of Operations to Sort a Binary Tree by Level
# Runtime: 169 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def getSwaps(l):
            sl = sorted(l)
            ind = {}
            swaps=0
            for i in range(len(l)):
                ind[l[i]] = i
            for i in range(len(l)):
                if l[i]!=sl[i]:
                    j = ind[sl[i]]
                    l[j],l[i] = l[i],l[j]
                    ind[l[j]] = j
                    ind[l[i]] = i
                    swaps+=1   
            # swaps = max(swaps-1,0)
            return swaps

        def dfs(nodes):
            children = []
            temp = []
            if not nodes:
                return
            for node in nodes:
                if node.left:
                    children.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    children.append(node.right)
                    temp.append(node.right.val)
            ans[0]+= getSwaps(temp)

            dfs(children)

        dfs([root])
        return ans[0]