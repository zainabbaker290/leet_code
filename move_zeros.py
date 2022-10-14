class Solution:
    def moveZeroes(self, nums):
        
        i = 0
        for n in nums:
            if n == 0:
                nums.remove(nums[i])
                nums.append(0)
            i+=1

                
        
        return nums

                

nums = [0,1,0,3,12]
S = Solution()
print(S.moveZeroes(nums))
