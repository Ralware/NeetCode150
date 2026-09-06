class Solution:
    def plusOne(self, Nums: List[int]) -> List[int]:

        Number = 0

        for Index in range(len(Nums)):
            Number = Number*10+Nums[Index]
        
        Nums[:] = []
        
        for Num in str(Number+1):
            Nums.append(int(Num))
        
        return Nums
        