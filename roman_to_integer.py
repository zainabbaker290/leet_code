roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

class Solution(object):
    def romanToInt(self, s):
        total = 0 
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                #taking away intial amount added and finding amount to actually add
                amount_to_add = (roman[s[i]] - roman[s[i-1]]) - roman[s[i - 1]] 
                total += amount_to_add
            else:
                total += roman[s[i]]
        
        return total


S = Solution()
print(S.romanToInt("IXIII"))
                
        