class Solution:
    def reverse(self, Num: int) -> int:

        if Num < 0:
            isNeg = True
            Num = abs(Num)
        else:
            isNeg = False

        Rev = int(str(Num)[::-1])

        if isNeg:
            Rev = -Rev

        if -2**31 <= Rev <= 2**31 - 1 :
            return Rev

        return 0 