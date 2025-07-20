# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        q = deque([root])  # queue for level-order traversal

        while q:
            for i in range(len(q)):  # iterate through current level
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1  # level completed

        return level






## Method-1: Using DFS Recursion
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         else:
#             val = (1+(max(self.maxDepth(root.left), self.maxDepth(root.right))))
#             return val
        