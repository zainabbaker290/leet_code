class Solution:
    def intersect(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)
        

                

            

        

S = Solution()
print(S.intersect([1,2,2,1], [2,2]))