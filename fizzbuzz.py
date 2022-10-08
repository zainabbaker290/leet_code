class Solution:
    def fizzBuzz(self, n: int):
        list_of_fizz = []
        num = 1  
        for i in range(n):
            if num % 3 == 0 and num % 5 == 0:
                list_of_fizz.append("FizzBuzz")
            elif num % 3 == 0:
                list_of_fizz.append("Fizz")
            elif num % 5 == 0:
                list_of_fizz.append("Buzz")
            else:
                list_of_fizz.append(str(num))       

            num += 1
        return list_of_fizz
S = Solution()
print(S.fizzBuzz(3))