class Solution:
    def merge(self, nums1,nums2) :
        for num in nums2:
            i = 0
            for n in nums1:
                if num >= n:
                    if i == len(nums1) - 1:
                        nums1.insert(i+1,num)
                        break
                        
                    elif num < nums1[i+1]:
                        nums1.insert(i,num)
                        break
                    
                    elif num == n:
                        nums1.insert(i + 1,num)
                        break
                    
                    else:
                        pass
                    
                i +=1       
            
        return nums1


