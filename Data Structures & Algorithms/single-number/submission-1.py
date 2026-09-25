class Solution:
    def singleNumber(self, Nums: List[int]) -> int:
        Seen = {}
        
        for Num in Nums:
            
            if Num in Seen:
                Seen[Num] = Seen[Num] + 1 
            elif not Num in Seen:
                Seen[Num] = 1
                
        for Index in Seen:
            if Seen[Index] == 1:
                return Index       