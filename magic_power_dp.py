"""Task 3"""

import math

def magic_power(string: str) -> int:
    """
    Сalculate the minimum number of ingredients needed to reach the desired magic power.
    :param string: A string where the first number is the desired magic power,
                   followed by the powers of available ingredients.
    :return: Minimum number of ingredients needed, or -1 if it's not possible.
    """

    splitted = string.split()
    power = int(splitted[0])
    dp = [math.inf] * (power + 1)
    dp[0] = 0

    for ingredient in splitted[1:]:
        ingredient_power = int(ingredient)
        for j in range(ingredient_power, power + 1):
            dp[j] = min(dp[j], dp[j - ingredient_power] + 1)

    return dp[power] if dp[power] != math.inf else -1

if __name__ == "__main__":
    assert magic_power("11 1 5 6") == 2  # 6 + 5

    assert magic_power("7 2 3") == 3  # 2+2+3

    assert magic_power("7 2 4") == -1

    assert magic_power("0 5 10") == 0

    assert magic_power("9 3") == 3  # 3+3+3

    print("All tests passed!")
