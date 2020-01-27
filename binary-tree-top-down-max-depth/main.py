class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

answer = 0

class Solution:
    def max_depth_td(self, root, depth):
        global answer
        if not root:
            return

        if not root.right and not root.left:
            answer =  max(answer, depth)

        if root.left:
            Solution().max_depth_td(root.left, depth + 1)
        
        if root.right:
            Solution().max_depth_td(root.right, depth + 1)
        
        return answer
        

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

result = Solution().max_depth_td(root, 1)
print(result)

# Should be 5