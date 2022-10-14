class Solution:
    def missingNumber(self, nums):
        max_num = max(nums)
        min_num = min(nums) 

        nums.sort()

        if len(nums) == 1:
            if nums[0] != 0:
                return max_num - 1

        i = 0
        for i in range(len(nums) -1):
            if min_num != 0:
                return 0
            elif nums[i +1] - nums[i] != 1:
                return nums[i +1] - 1
            i +=1
        
        else:
            return max_num + 1
        
        



nums = [1,2]
S = Solution()
print(S.missingNumber(nums))