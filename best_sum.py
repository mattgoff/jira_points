def best_sum(targetSum, numbers):
    return _best_sum(targetSum, numbers, dict())


def _best_sum(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortest_combo = None

    for num in numbers:
        remainder = targetSum - num
        remainder_combo = _best_sum(remainder, numbers, memo)

        if remainder_combo is not None:
            combination = [*remainder_combo, num]
            if shortest_combo is None or len(combination) < len(shortest_combo) :
                shortest_combo = combination

    memo[targetSum] = shortest_combo
    return memo[targetSum]


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))


