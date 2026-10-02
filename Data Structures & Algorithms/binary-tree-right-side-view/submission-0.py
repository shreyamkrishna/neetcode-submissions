# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        curr = deque()
        curr.append(root)
        result = []
        while len(curr)>0:
            length = len(curr)
            for i in range(len(curr)):
                node = curr.popleft()
                                
                if length -1 == i:
                    result.append(node.val)

                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
        
        return result
                