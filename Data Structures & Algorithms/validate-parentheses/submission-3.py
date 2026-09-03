class Solution:
    def isValid(self, Brackets: str) -> bool:
        Stack = []

        BracketSet = {"{", "[", "("}

        Data = {"}": "{", "]": "[", ")": "("}

        for Bracket in Brackets:

            if Bracket in BracketSet:
                Stack.append(Bracket)

            else:

                if not Stack:
                    return False

                if Stack[-1] == Data[Bracket]:
                    Stack.pop()
                else:
                    return False

        return len(Stack) == 0