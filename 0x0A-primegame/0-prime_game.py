#!/usr/bin/python3
"""Prime game function"""


def is_prime(num):
    """
    Check if a number is prime
    Args:
        num: array of numbers
    Return: true / false
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def play_round(n):
    """
    Simulate a single round of the game
    Args:
         n: number of players
    Return: bool
    """
    primes = [i for i in range(1, n + 1) if is_prime(i)]
    turn = 0  # 0 for Maria, 1 for Ben
    while primes:
        prime = primes.pop(0)
        primes = [x for x in primes if x % prime != 0]
        turn = 1 - turn
    return turn  # 0 if Ben wins, 1 if Maria wins

def isWinner(x, nums):
    """
    Determine the winner of the most rounds

    Args:
        x: number of rounds
        nums: an array of n
    Return: winner or none
    """
    if not nums or x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_round(n) == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None