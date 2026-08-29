class Solution:
    def search(self, Nums: List[int], Target: int) -> int:
        Low = 0
        High = len(Nums) - 1

        while High >= Low:
            Mid = (Low + High)//2

            if Nums[Mid] > Target:
                High = Mid - 1
            elif Nums[Mid] < Target:
                Low = Mid + 1
            else:
                return Mid
        
        return -1