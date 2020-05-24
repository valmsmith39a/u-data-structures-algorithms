"""
# Coin Change

You are given coins of different denominations and a total amount of money. Write a function to compute the fewest coins needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

As an example:
* Input: `coins = [1, 2, 3]`, `amount = 6`
* Output: `2`
* Explanation: The output is `2` because we can use `2` coins with value `3`. That is, `6 = 3 + 3`. We could also use `3` coins with value `2` (that is, `6 = 2 + 2 + 2`), but this would use more coins—and the problem specifies we should use the smallest number of coins possible.

There's test code below that you can use to check your solution. And at the bottom of the notebook, you'll find two different possible solutions.
"""


def coin_change(coins, amount):

    # TODO: Complete the coin_change function
    # This should return one value: the fewest coins needed to make up the given amount

    # create a memo to store pre-computed fewest coins needed to make a given amount
    memo = {}

    def return_change(remaining):

        if remaining < 0:
            return float('inf')

        if remaining == 0:
            return 0

        if remaining not in memo:
            memo[remaining] = min(return_change(
                remaining - c) + 1 for c in coins)
            print(memo)
        return memo[remaining]

    res = return_change(amount)

    return -1 if res == float('inf') else res


def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)

arr = [1, 4, 5, 6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)

arr = [5, 7, 8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)
