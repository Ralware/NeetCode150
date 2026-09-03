class Solution:
    def evalRPN(self, Operations: List[str]) -> int:
        Stack = []

        Operators = {"*", "/", "+", "-"}

        for Operation in Operations:

            if Operation not in Operators:
                Stack.append(int(Operation))

            else:

                Right = Stack.pop()
                Left = Stack.pop()

                if Operation == "*":
                    Stack.append(Left * Right)

                elif Operation == "/":
                    Stack.append(int(Left / Right))

                elif Operation == "+":
                    Stack.append(Left + Right)

                else:
                    Stack.append(Left - Right)

        return Stack[0]