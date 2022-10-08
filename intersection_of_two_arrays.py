class Solution:
    def intersect(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)

        for num in nums1:
            for n in nums2:
                if n == num:
                    print(n, num)

            
        return

S = Solution()
print(S.intersect([1,2,2,1], [2,2]))