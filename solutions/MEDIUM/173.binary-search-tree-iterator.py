# Problem ID: 173
# Title: Binary Search Tree Iterator
# Runtime: 4 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.l.append(root.val)
        self.inorder(root.right)

    def __init__(self, root: Optional[TreeNode]):
        self.l = []
        self.inorder(root)
        self.pointer = -1
    
    def next(self) -> int:
        self.pointer+=1
        return self.l[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer < len(self.l)-1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()