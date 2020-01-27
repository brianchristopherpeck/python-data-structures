class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def max_depth_td(self, root):
        if not root:
            return 0
        else:
            left_depth = self.max_depth_td(root.left)
            right_depth = self.max_depth_td(root.right)
            return max(left_depth, right_depth) + 1
        
        

# Tree Node
#          3
#        /   \
#       9     20
#      / \    / \
#     7   6  15   17
#        /       /
#       11      14
#                \
#                 2

root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(11)

root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(17)
root.right.right.left = TreeNode(14)
root.right.right.left.right = TreeNode(2)

result = Solution().max_depth_td(root)
print(result)

# Should be 5