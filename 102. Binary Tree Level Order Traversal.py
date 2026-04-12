# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Base case: if tree is empty [00:04:57]
        if not root:
            return []
        
        # Initialize queue with root [00:05:13]
        q = deque([root])
        answer = []
        
        while q:
            level = []
            # 'n' is the number of nodes at the CURRENT level [00:06:11]
            n = len(q)
            
            for _ in range(n):
                node = q.popleft() # Pop from the LEFT to keep it O(1) [00:07:03]
                level.append(node.val)
                
                # Queue up the children for the NEXT level [00:07:30]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # After finishing one level, add it to the final result [00:07:59]
            answer.append(level)
            
        return answer