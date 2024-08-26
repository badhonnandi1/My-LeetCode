class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            if nums[i] in mydict.keys():
                if nums[i] + nums[i] == target:
                    return [mydict[nums[i]],i]
            mydict[nums[i]] = i

        nums.sort()
        start = 0
        end = len(nums) - 1

        while start < end:
            if nums[start] + nums[end] < target:
                start += 1
            elif nums[start] + nums[end] > target:
                end -= 1 
            else:
                return [mydict[nums[start]],mydict[nums[end]]]

# Driver code
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)
    

# solved with order of nlogn
#space complexity is O(n)