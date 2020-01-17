class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def preorderTraversalRecursive(self, root):
        output = []
        Solution().printInorder(root, output)
        return output
        
    def printInorder(self, root, output): 
        
        if root: 
      
            # then print the data of node 
            output.append(root.val)
    
            # First recur on left child 
            Solution().printInorder(root.left, output) 
      
            # now recur on right child 
            Solution().printInorder(root.right, output)

# Tree Node
#         3
#        / \
#       9   20
#           /\
#         15  17


root = TreeNode(3)
root.left = TreeNode(9)

root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(17)


result = Solution().preorderTraversalRecursive(root)
print(result)

# output
#[3, 9, 20, 15, 17]