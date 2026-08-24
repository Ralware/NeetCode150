class Solution:
    def isPalindrome(self, Word: str) -> bool:
        Low = 0
        High = len(Word)-1
        Word = Word.lower() 

        while Low < High:

            if not Word[High].isalnum():
                High-=1
                continue
            if not Word[Low].isalnum():
                Low+=1
                continue

            if Word[High] == Word[Low]:
                High-=1
                Low+=1
                continue
            else:
                return False
        
        return True
        