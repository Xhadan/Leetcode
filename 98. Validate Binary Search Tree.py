# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function with boundary limits [00:06:03]
        def is_valid(node, minimum, maximum):
            # Base Case: An empty tree is a valid BST [00:03:53, 00:06:21]
            if not node:
                return True
            
            # Check if current node violates its boundaries [00:06:28]
            if not (minimum < node.val < maximum):
                return False
            
            # Recursively check left and right subtrees with updated bounds [00:06:46]
            return (is_valid(node.left, minimum, node.val) and 
                    is_valid(node.right, node.val, maximum))

        # Start with negative and positive infinity [00:06:13, 00:07:36]
        return is_valid(root, float('-inf'), float('inf'))
        