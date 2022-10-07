#get square root 
#only integer part returned 
#cant use 
from math import sqrt, trunc

class Solution:
    def mySqrt(self, x): 
        sq_root = sqrt(x)
        sq_root = trunc(sq_root)
        
        return sq_root

S = Solution()
print(S.mySqrt(133))

