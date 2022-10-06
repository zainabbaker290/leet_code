class Solution(object):
    def isValid(self, s):
        stack_list = []
        if len(s) > 0 and (len(s) % 2) == 0:
            for item in s:
                if item == "[" or item == "{" or item == "(":
                    stack_list.append(item)
                elif len(stack_list) == 0 and item == "]" or len(stack_list) == 0 and item == "}" or len(stack_list) == 0 and item == ")":
                    return False
                elif item == "]":
                    if stack_list[-1] == "[":
                        stack_list.pop()
                    else:
                        return False
                elif item == ")":
                    if stack_list[-1] == "(":
                        stack_list.pop()
                    else:
                        return False
                elif item == "}":
                    if stack_list[-1] == "{":
                        stack_list.pop()
                    else:
                        return False
        
            if len(stack_list) == 0:
                return True
        
        return False
S = Solution()
print(S.isValid("]{"))