# Problem ID: 1387
# Title: Find Elements in a Contaminated Binary Tree
# Runtime: 7 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.mp = set([0])
        self.root = root
        self.recoverTree()
        

    def recoverTree(self):
        def dfs(node,val):
            if not node:
                return 
            node.val = val
            self.mp.add(val)
            dfs(node.left, val * 2 + 1)
            dfs(node.right, val * 2 +2)
        dfs(self.root, 0)

    def find(self, target: int) -> bool:
        if target in self.mp:
            return True   
        return False



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)