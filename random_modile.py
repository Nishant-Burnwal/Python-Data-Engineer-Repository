# PROG 1.1: To Implement Single Function

import random

def run_flip_a_coin(n):
    """
        Description: Flips a coin
        Parameters: coin flip times
        Return: Print the percentage of head coin in flipping a coin
    """
    head_count = 0
    for _ in range(n):
        coin_sides_list = ["HEAD", "TAIL"]
        result = random.choice(coin_sides_list)
        if result == "HEAD":
            head_count += 1

    percentage_head_count = (head_count / n) * 100
    print(f"After flipping the coin {n} times, the percentage of time head has come is {percentage_head_count:.2f}%")

coin_flip_times = int(input("Enter the number of times to flip the coin: "))

run_flip_a_coin(coin_flip_times)