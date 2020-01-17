class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversalRecursive(self, root):
        output = []
        Solution().printInorder(root, output)
        return output
        
    def printInorder(self, root, output): 
        
        if root: 
      
            # First recur on left child 
            Solution().printInorder(root.left, output) 
      
            # now recur on right child 
            Solution().printInorder(root.right, output)
            
            # then print the data of node 
            output.append(root.val)

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


result = Solution().postorderTraversalRecursive(root)
print(result)

# output
# [9, 15, 17, 20, 3]