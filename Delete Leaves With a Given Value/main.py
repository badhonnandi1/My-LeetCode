# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root, target: int):
        def removeNode(root,tg):
            if not root:
                return
            
            if root.left and root.left.val == target:
                if not root.left.left and not root.left.right:
                    root.left = None
            
            if root.right and root.right.val == target:
                if not root.right.left and not root.right.right:
                    root.right = None
            
            removeNode(root.left,tg)
            removeNode(root.right,tg)
            
        def inorder(root,ct):
            if not root:
                return 
            
            inorder(root.left,ct)
            ct[0] += 1
            inorder(root.right,ct)
        
        ct = [0]
        inorder(root,ct)
        
        for i in range(ct[0]):
            removeNode(root,target)
        if not root.left and not root.right and root.val == target:
            return None
        return root

mySolution = Solution()
root = [1,2,3,2,'null',2,4] 
target = 2
print(mySolution.removeLeafNodes(root,target))
