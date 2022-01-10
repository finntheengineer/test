class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : 
            return False
        elif x % 10 == 0 and x !=0:
            return False
        y = 0
        z = x
        while x > y:
            y = y*10 + x%10
            z = x
            x = x//10
        return x == y or z == y