# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Using a list to act as a shared variable across recursion [00:05:33]
        count = [k]
        answer = [0]

        def dfs(node):
            if not node:
                return
            
            # Step 1: Go all the way to the Left [00:06:05]
            dfs(node.left)

            # Step 2: Process the current Node [00:06:15]
            if count[0] == 1:
                answer[0] = node.val
                # Decrement to 0 so we stop exploring [00:07:09]
                count[0] -= 1
                return
            
            count[0] -= 1

            # Step 3: Go to the Right only if we haven't found the answer yet [00:06:45]
            if count[0] > 0:
                dfs(node.right)

        dfs(root)
        return answer[0]