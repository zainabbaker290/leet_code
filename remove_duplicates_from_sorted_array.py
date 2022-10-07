class Solution(object):
    def removeDuplicates(self, nums):
        i = 0 
        removed = 0 
        for num in nums:
            if i < len(nums) - 1:
                for right_int in nums[i+1:]:
                    if num == right_int and type(right_int) == int: 
                        nums.remove(right_int)
                        nums.append("_")
                        removed += 1
                i += 1
    
        count = len(nums) - removed
        return count


S = Solution()
print(S.removeDuplicates([1,1,1,2,3,4,4]))
