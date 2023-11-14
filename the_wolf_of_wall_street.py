def sum_two(stock_prices_yesterday, target):
    for i in range(len(stock_prices_yesterday)):
        for j in range(i+1, len(stock_prices_yesterday)):
            result = stock_prices_yesterday[j]-stock_prices_yesterday[i]
            if result == target:
                return stock_prices_yesterday[i], stock_prices_yesterday[j]
                

def get_max_profit(stock_prices_yesterday):
    result_before = 0
    for i in range(len(stock_prices_yesterday)):
        for j in range(i+1, len(stock_prices_yesterday)):
            result_after = stock_prices_yesterday[j]-stock_prices_yesterday[i]
            if result_after > result_before:
                result_before = result_after
            else:
                pass
    sum = sum_two(stock_prices_yesterday, result_before)
    return sum[0], sum[1], result_before
            
            

print(get_max_profit([1, 2, 3, 4, 5, -10]))