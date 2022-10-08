class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dic = {}
        for char in s:
            if char in count_dic.keys():
                count_dic[char] += 1
            else:
                count_dic[char] = 1
        
        unique_letter = ""
        for key, val in count_dic.items():
            if val == 1:
                unique_letter = key
                break 
        
        pos = s.index(unique_letter)

        return pos

S = Solution()
print(S.firstUniqChar("loveleetcode"))