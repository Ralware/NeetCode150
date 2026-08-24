class Solution:
    def twoSum(self, Nums: List[int], Target: int) -> List[int]:

        Low = 0
        High = len(Nums)-1

        while Low < High:

            Sum = Nums[Low] + Nums[High]

            if Sum == Target:
                return [Low+1,High+1]
            elif Sum < Target:
                Low+=1
            else:
                High-=1

