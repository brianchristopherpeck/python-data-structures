# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool: 
        return self.isMirror(root, root)
    
    def isMirror(self, t1: TreeNode, t2: TreeNode):
        if t1 is None and t2 is None: 
            return True
        if t1 is None or t2 is None: 
            return False
        
        return (t1.val == t2.val) and self.isMirror(t1.right,t2.left) and self.isMirror(t1.left,t2.right)

# Tree Node
#          3
#        /   \
#       9     9
#      / \    / \
#     7   6  6   7
#        /    \  
#       11     11 
 


root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(11)

root.right = TreeNode(9)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(11)

result = Solution().isSymmetric(root)
print(result)