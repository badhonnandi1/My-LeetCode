class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        myset = set()
        for i in nums:
            if i not in myset:
                myset.add(i)

        for i in range(len(nums)):
            nums[i] = 0
        
        x = 0
        mylist = list(myset)
        mylist.sort()
        
        for i in mylist:
            nums[x] = i
            x += 1

        return x 

if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    solution = Solution()
    result = solution.removeDuplicates(nums)
    print(result)
    print(nums[:result])

# solved with order of nlong
#space complexity is O(n)
