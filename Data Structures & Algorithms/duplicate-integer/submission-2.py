class Solution:
    def hasDuplicate(self, Nums: List[int]) -> bool:
        
        Seen = set()

        for Value in Nums:

            if not Value in Seen:
                Seen.add(Value)    
            else:
                return True

        return False