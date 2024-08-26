class Solution:
    def removeDuplicates(self, nums):
        def leftshift(mylist,x):
            for i in range(x,len(mylist)):
                mylist[i-1] = mylist[i]
            mylist[len(mylist)-1] = '_'


        x = 1

        while x < len(nums) - 1:
            if nums[x-1] == nums[x]:
                leftshift(nums,x)            
            x += 1
        print(nums)
        for i in range(len(nums)):
            if nums[i] == '_':
                return i
    
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    solution = Solution()
    result = solution.removeDuplicates(nums)
    print(result)
    print(nums[:result])

