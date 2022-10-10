class Solution:
    def isPalindrome(self, s: str) -> bool:

        replace_dict = {" ": "", "," : "", ":" : " "}

        for string in s:
            if string in replace_dict.keys(): 
               s = s.replace(string, replace_dict[string])
            
            s = s.lower()
        
        i = 0 
        j = len(s) - 1
        for string in range(len(s)):
            print(s[i],s[j])
            if s[i] == s[j]:
                
                i += 1
                j -= 1
            else: 
                return False

        return True
        



s = "A man, a plan, a canal: Panama"
S = Solution()
print(S.isPalindrome(s))
