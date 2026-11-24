# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def bfs(root):
            q = deque()
            res = []

            if root:
                q.append(root)

            while len(q) > 0:
                for i in range(len(q)):
                    curr = q.popleft()
                    if curr:
                        res.append(curr.val)
                    else:
                        res.append(curr)
                        continue
                    
                    if curr.left:
                        q.append(curr.left)
                    else:
                        q.append(None)

                    if curr.right:
                        q.append(curr.right)
                    else:
                        q.append(None)
            return res

        print(bfs(p))
        print(bfs(q))
        return bfs(p) == bfs(q)
                


            

            

            
        