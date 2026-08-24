class Solution:
    def productExceptSelf(self, Nums: List[int]) -> List[int]:

        ZeroCount = 0
        Product = 1
        for Value in Nums:
            if Value != 0:
                Product = Product * Value
            else:
                ZeroCount+=1
        
        for Index in range(len(Nums)):
            if Nums[Index] != 0 and ZeroCount == 0:
                Nums[Index] = int(Product / Nums[Index])
            
            elif Nums[Index] != 0 and ZeroCount > 0:
                Nums[Index] = 0 
                
            elif Nums[Index] == 0 and ZeroCount == 1:
                        Nums[Index] = Product               
        
        return Nums
        