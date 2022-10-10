import math

class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        elif math.log(n,3) % 1 == 0:
            return True
        else:
            return False
        


S = Solution()
print(S.isPowerOfThree(243))