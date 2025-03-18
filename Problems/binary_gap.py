class BinaryGap:
    def binaryGap(self, n: int) -> int:
        N = bin(n)[2:]
        print("Binary: ", N)
        b = 0
        max_b = 0
        for i in N:
            if int(i) == 0:
                b += 1
            elif int(i) == 1:
                max_b = max(b, max_b)
                b = 1
        return max_b