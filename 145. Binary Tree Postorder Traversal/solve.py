class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def selfmade(root,arr):
            if not root:
                return
            
            selfmade(root.left,arr)   
            selfmade(root.right,arr)
            arr.append(root.val)
        
        arr = []
        selfmade(root,arr)
        return arr

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    solution = Solution()
    
    result = solution.postorderTraversal(root)
    print(result)