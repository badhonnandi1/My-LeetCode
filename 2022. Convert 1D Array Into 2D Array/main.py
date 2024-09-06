class Solution:
    def construct2DArray(self, original, m , n ):
        array = [[0] * n for _ in range(m)]
        if m*n != len(original):
            return []
    
        x = 0
        r = 0
        c = 0
        for i in original:
            r = x // n
            c = x % n
            array[r][c] = i
            x += 1

        return array

original = [1,2,3,4]
m = 2
n = 2
main = Solution(original,m,n)
print(main)