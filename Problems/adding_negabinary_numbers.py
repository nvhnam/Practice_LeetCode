import math
from typing import List


class AddingNegaBinaryNumber:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num1 = 0
        num2 = 0

        count1 = len(arr1) - 1
        count2 = len(arr2) - 1

        for i in arr1:
            if i == 0:
                count1 -= 1
            else:
                num1 += (-2)**count1
                count1 -= 1
        print("Num1: ", num1)

        for i in arr2:
            if i == 0:
                count2 -= 1
            else:
                num2 += (-2)**count2
                count2 -= 1
        print("Num2: ", num2)

        sum = num1 + num2
        print("Sum: ", sum)
        if sum == 0:
            return [0]
        stack = []
        def to_binary(num):
            quotient = num // (-2)
            remainder = num % (-2)
            # print("remainder: ", remainder)

            if remainder < 0:
                remainder = abs(remainder)
                quotient += 1

            stack.append(remainder)
            if quotient != 0:
                to_binary(quotient)
        
        to_binary(sum)
        stack.reverse()

        return stack
        