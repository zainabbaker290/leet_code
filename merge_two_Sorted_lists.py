class Solution(object):
    def mergeTwoLists(self, list1, list2):     
        for num in list1:
            for n in list2:
                i = list2.index(n)
                if num > n:
                    continue
                else:
                    list2.insert(i, num)
                    break
        
        return(list2)

S = Solution()
print(S.mergeTwoLists([1,2,4],[1,3,4]))