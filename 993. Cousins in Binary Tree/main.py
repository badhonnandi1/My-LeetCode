# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def lvlOrder(root):
            if not root:
                return
            final = []
            queue = [root]

            while queue:
                lvl = []
                for i in range(len(queue)):
                    node = queue.pop(0)
                    lvl.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                final.append(lvl)
            return final
                    

        def findparent(root):
            parentdict = {}
            def dfs(root,parent=None):
                if not root:
                    return
                parentdict[root.val] = parent.val if parent else None
                dfs(root.left,root)
                dfs(root.right,root)
            dfs(root)
            return parentdict
        takeaway = findparent(root)

        lvl = lvlOrder(root)
        for i in lvl:
            if takeaway[x] != takeaway[y]:
                if x in set(i) and y in set(i):
                    return True
        return False

                

