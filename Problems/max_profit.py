class MaxProfit:
    def max_profit(self, prices: list[int]) -> int:
        self.prices = prices

        arr = self.prices
        left = 0 
        right = 1
        profit = 0
        while right < len(arr):
            if(arr[right] < arr[left]):
                left = right
            if(arr[right] > arr[left]):
                temp = arr[right] - arr[left]
                if(temp > profit):
                    profit = temp
            right += 1
        return profit