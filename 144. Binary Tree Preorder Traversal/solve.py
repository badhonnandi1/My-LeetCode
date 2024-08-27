# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def selfmade(root,arr):
            if not root:
                return
            arr.append(root.val)
            selfmade(root.left,arr)
            selfmade(root.right,arr)
        
        my = []
        selfmade(root,my)
        return my
            
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create an instance of the Solution class
    solution = Solution()

    # Call the preorderTraversal method and print the result
    result = solution.preorderTraversal(root)
    print(result)
