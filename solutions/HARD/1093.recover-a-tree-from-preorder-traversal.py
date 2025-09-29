# Problem ID: 1093
# Title: Recover a Tree From Preorder Traversal
# Runtime: 11 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        root = TreeNode(int(traversal[0]))
        st = []
        i, n = 0, len(traversal)
        dashes = 0
        while i<n:
            if traversal[i] == "-":
                dashes+=1
                i+=1
            else:
                j = i
                while j<n and traversal[j]!="-":
                    j+=1
                val = int(traversal[i:j])
                node = TreeNode(val)
                
                while len(st) > dashes:
                    st.pop()
                
                if st and not st[-1].left:
                    st[-1].left = node
                elif st and not st[-1].right:
                    st[-1].right = node
                st.append(node)
                i = j
                dashes = 0
        return st[0]