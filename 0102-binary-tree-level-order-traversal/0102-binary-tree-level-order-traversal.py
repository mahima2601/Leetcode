# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que=deque([root])
        result=[]
        if not root:
            return []
        while que:
            que2 = deque()
            level = []
            while que:
                node=que.popleft()
                if node:
                    level.append(node.val)
                    que2.append(node.left)
                    que2.append(node.right)
            if level: 
                result.append(level)
            que = que2
        return result
            


        