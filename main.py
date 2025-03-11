from Problems import MaxProfit

def main():
    max_profit_calculator = MaxProfit()

    prices = [7, 1, 5, 3, 6, 4]

    result = max_profit_calculator.max_profit(prices)
    print("Max Profit:", result)

main()