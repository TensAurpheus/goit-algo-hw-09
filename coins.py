from timeit import timeit

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(sum_: int):
    count_coins = {}
    for coin in coins:
        count = sum_ // coin
        if count > 0:
            count_coins[coin] = count
        sum_ = sum_ - coin * count
    return count_coins


def find_coins_dynamic(sum_):
    # Тут індекс це сума
    min_coins_required = [0] + [float("inf")] * sum_  # мінімальна кілкість монет
    last_coin_used = [0] * (sum_ + 1)  # остання монета для цієї суми

    for s in range(1, sum_ + 1):
        for coin in coins:
            if coin <= s and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin

    current_sum = sum_
    coin_list = {}

    while current_sum > 0:
        coin = last_coin_used[current_sum]
        coin_list[coin] = coin_list.get(coin, 0) + 1
        current_sum -= coin
    
    return coin_list

if __name__ == "__main__":
    # discrepancies = []
    # for sum in range(1, 10000):
    #     if find_coins_greedy(sum) != find_coins_dynamic(sum):
    #         discrepancies.append(sum)
    # print(discrepancies)

    sum_small = 123
    sum_medium = 12345
    sum_large = 1234567
    repeat = 1

    time_small_greedy = timeit(lambda: find_coins_greedy(sum_small), number=repeat)
    time_small_dynamic = timeit(lambda: find_coins_dynamic(sum_small), number=repeat)
    time_medium_greedy = timeit(lambda: find_coins_greedy(sum_medium), number=repeat)
    time_medium_dynamic = timeit(lambda: find_coins_dynamic(sum_medium), number=repeat)
    time_large_greedy = timeit(lambda: find_coins_greedy(sum_large), number=repeat)
    time_large_dynamic = timeit(lambda: find_coins_dynamic(sum_large), number=repeat)

    print(f"| {'Algorithm': <20} | {'Time small (' + str(sum_small) + ')': <20} | {'Time medium (' + str(sum_medium) + ')': <20} | {'Time large (' + str(sum_large) + ')': <20} |")
    print(f"|{'-'*22}|{'-'*22}|{'-'*22}|{'-'*22}|")
    print(f"| {'Greedy': <20} | {time_small_greedy: <20.7f} | {time_medium_greedy: <20.7f} | {time_large_greedy: <20.7f} |")
    print(f"| {'Dynamic': <20} | {time_small_dynamic: <20.7f} | {time_medium_dynamic: <20.7f} | {time_large_dynamic: <20.7f} |")
 
    sum = 87
    result_greedy = find_coins_greedy(sum)
    result_dynamic = find_coins_dynamic(sum)
    print(f'Greedy({sum}): {result_greedy}')
    print(f'Dynamic({sum}): {result_dynamic}')
    