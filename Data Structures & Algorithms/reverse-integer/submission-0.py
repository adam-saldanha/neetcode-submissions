class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            limit = 2**31 - 1
        else:
            sign = 1
            limit = 2**31

        res = 0
        x = abs(x)

        while x:
            digit = x % 10
            x = x // 10
            if res > limit // 10 or ( res == limit // 10 and digit > limit % 10):
                return 0
            res = res * 10 + digit
        return sign * res


        