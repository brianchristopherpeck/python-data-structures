import collections

class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = collections.deque([root,])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)

            for _ in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels

# Tree Node
#          3
#        /   \
#       9     20
#      / \    / \
#     7   6  15   17


root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)

root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(17)


result = Solution().levelOrder(root)
print(result)