class Solution:
    def isHappy(self, Num: int) -> bool:

        Seen = set()
    
        def Sum(Num):
            Digits_Sum = 0
            for Digit in str(Num):
                Digits_Sum += (int(Digit))**2
            return Digits_Sum
        
        Calc_Sum = Sum(Num)
        
        while  Calc_Sum != 1:
            if Calc_Sum in Seen:
                return False
            
            Seen.add(Calc_Sum)
            
            Calc_Sum = Sum(Calc_Sum)
            
        return True

        