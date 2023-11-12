def find_arbitrage_opportunity(rate_matrix):
    rate_1 = rate_matrix[0][1]
    rate_2 = rate_matrix[1][2]
    rate_3 = rate_matrix[2][0]

    arbitrage_opportunity = rate_1 * rate_2 * rate_3

    return arbitrage_opportunity

def execute_arbitrage(balance, rate_matrix):
    amount_to_trade = balance

    amount_bought_1 = amount_to_trade
    amount_sold_2 = amount_bought_1 / rate_matrix[0][1]
    amount_sold_3 = amount_sold_2 / rate_matrix[1][2]
    amount_bought_back_1 = amount_sold_3 * rate_matrix[2][0]

    print("Arbitrage opportunity found and executed!")
    print(f"Initial balance: {balance}")
    print(f"Final balance: {amount_bought_back_1}")
def main():
    rate_matrix = [
        [1, 2, 0.5],
        [0.5, 1, 3],
        [2, 0.33, 1]
    ]
    balance = 1

    while True:
        arbitrage_opportunity = find_arbitrage_opportunity(rate_matrix)
        print(f"Arbitrage opportunity: {arbitrage_opportunity}")

        if arbitrage_opportunity > 1:
            execute_arbitrage(balance, rate_matrix)


            time.sleep(10)


if __name__ == "__main__":
    import time
    main()
