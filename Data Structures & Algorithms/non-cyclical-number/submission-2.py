class Solution:
    def isHappy(self, Num: int) -> bool:

        Seen = set()
    
        def Sum(Num):
            Total = 0

            while Num:
                Digit = Num % 10
                Total += Digit ** 2
                Num //= 10

            return Total

        Calc_Sum = Sum(Num)

        while  Calc_Sum != 1:
            if Calc_Sum in Seen:
                return False

            Seen.add(Calc_Sum)

            Calc_Sum = Sum(Calc_Sum)

        return True

        