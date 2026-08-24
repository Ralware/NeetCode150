class Solution:
    def isAnagram(self, First: str, Second: str) -> bool:
        
        First_Data = {}
        Second_Data = {}

        if len(First) != len(Second):
            return False

        for Index in range(len(First)):
            if not First[Index] in First_Data:
                First_Data[First[Index]] = 1

            elif First[Index] in First_Data:
                First_Data[First[Index]] += 1     
            
            if not Second[Index] in Second_Data:
                Second_Data[Second[Index]] = 1
            
            elif Second[Index] in Second_Data:
                Second_Data[Second[Index]] += 1 

        return First_Data == Second_Data
        