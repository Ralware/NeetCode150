class Solution:
    def isValid(self, Brackets: str) -> bool:
        
        Stack = []

        Data = {"}": "{", "]": "[", ")": "("}

        for Bracket in Brackets:

            if Bracket =="{" or Bracket =="[" or Bracket =="(" :
                Stack.append(Bracket)

            else:

                if not Stack:
                    return False

                if Stack[-1] == Data[Bracket]:
                    Stack.pop()
                else:
                    return False

        return len(Stack) == 0