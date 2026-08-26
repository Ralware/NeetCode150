class Solution:
    def multiply(self, Num1: str, Num2: str) -> str:
        
        def GetInt(Number):
                
            IntNum = 0

            for Num in Number:
                if Num == "1":
                    IntNum = IntNum*10 + 1
                elif Num == "2":
                    IntNum = IntNum*10 + 2
                elif Num == "3":
                    IntNum = IntNum*10 + 3
                elif Num == "4":
                    IntNum = IntNum*10 + 4
                elif Num == "5":
                    IntNum = IntNum*10 + 5
                elif Num == "6":
                    IntNum = IntNum*10 + 6
                elif Num == "7":
                    IntNum = IntNum*10 + 7
                elif Num == "8":
                    IntNum = IntNum*10 + 8
                elif Num == "9":
                    IntNum = IntNum*10 + 9
                else:
                    IntNum = IntNum*10 + 0

            return IntNum
                
        IntNum1 = GetInt(Num1)
        IntNum2 = GetInt(Num2)

        Product = IntNum1*IntNum2

        if Product == 0:
            return "0"

        StringProduct = ""

        while Product > 0:
            Digit = Product % 10 

            if Digit == 1:
                StringProduct = "1" + StringProduct
            elif Digit == 2:
                StringProduct = "2" + StringProduct
            elif Digit == 3:
                StringProduct = "3" + StringProduct
            elif Digit == 4:
                StringProduct = "4" + StringProduct
            elif Digit == 5:
                StringProduct = "5" + StringProduct
            elif Digit == 6:
                StringProduct = "6" + StringProduct
            elif Digit == 7:
                StringProduct = "7" + StringProduct
            elif Digit == 8:
                StringProduct = "8" + StringProduct
            elif Digit == 9:
                StringProduct = "9" + StringProduct
            else:
                StringProduct = "0" + StringProduct

            Product = Product // 10
    
        return StringProduct
                