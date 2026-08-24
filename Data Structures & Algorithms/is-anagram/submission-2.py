class Solution:
    def isAnagram(self, First: str, Second: str) -> bool:
        
        First_Data = {}
        Second_Data = {}

        for Letter in First:
            if not Letter in First_Data:
                First_Data[Letter] = 1

            elif Letter in First_Data:
                First_Data[Letter] += 1   

        for Letter in Second:
                if not Letter in Second_Data:
                    Second_Data[Letter] = 1

                elif Letter in Second_Data:
                    Second_Data[Letter] += 1   

        return First_Data == Second_Data
        