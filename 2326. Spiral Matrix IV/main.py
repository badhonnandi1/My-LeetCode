# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
            spiral_matrix = [[-1 for _ in range(n)] for _ in range(m)]
            temp = head
            arr = []
            while temp:
                arr.append(temp.val)
                temp = temp.next
            
            top,left,idx = 0,0,0
            bottom = m - 1
            right = n - 1

            while top <= bottom and left <= right:
                for i in range(left, right+1):
                    if idx < len(arr):
                        spiral_matrix[top][i] = arr[idx]
                        idx += 1
                top += 1

                for i in range(top,bottom+1):
                    if idx < len(arr):
                        spiral_matrix[i][right] = arr[idx]
                        idx += 1
                right -= 1
                
                if top <= bottom:
                    for i in range(right,left - 1, -1):
                        if idx < len(arr):
                            spiral_matrix[bottom][i] = arr[idx]
                            idx += 1
                    bottom -= 1
                
                if left <= right:
                    for i in range(bottom,top - 1,- 1):
                        if idx < len(arr):
                            spiral_matrix[i][left] = arr[idx]
                            idx += 1
                    left += 1

            return spiral_matrix
