class Solution(object):
    def twoSum(self, nums, target):
        index_list = []
        counting_target = 0 
        l = len(nums) - 1
        for i,n in enumerate(nums):
            x = i +1 #keep track of where j is in list 
            for j in nums[i+1::]:
                counting_target = n + j
                if counting_target == target:
                    index_list.append(nums.index(n))
                    index_list.append(x) #if just do index for j, returns first occurence of j and not actual pos
                    return index_list
                else:
                    counting_target = 0
                    x += 1


S = Solution()
print(S.twoSum([3,3],6) )
