class Solution:
   def maxArea(self,Height):

    Low,High = 0, len(Height) - 1
    Area = 0

    while Low < High:
        Area = max(Area, (High - Low) * min(Height[Low], Height[High]))
        
        if Height[Low] < Height[High]:
            Low += 1
        else:
            High -= 1

    return Area