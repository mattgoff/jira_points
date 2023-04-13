def all_sum(task_count, targetSum, numbers):
    return _all_sum(task_count, targetSum, numbers, dict())


def _all_sum(target_count, targetSum, numbers, memo):
    if targetSum in memo:
        # print(f'Cache hit at {targetSum=}')
        return memo[targetSum]
    if targetSum == 0:
        return [[]]
    if targetSum < 0:
        return None

    all_combinations = []

    for num in numbers:
        remainder = targetSum - num
        remainder_combinations = _all_sum(target_count, remainder, numbers, memo)

        if remainder_combinations is not None:
            for combination in remainder_combinations:
                if len(combination) < target_count:
                    all_combinations.append(combination + [num])

    memo[targetSum] = all_combinations
    return memo[targetSum]


valid_combinations = []
fibinaci_seq = [1, 2, 3, 5, 8, 13, 21, 34]

#  There are 4 Jira Tasks, Totaling 29 points and each of the 4 tasks can have only Fib numbers as point values
all_combos_less_than_or_equal_target_count = all_sum(4, 29, fibinaci_seq)
[
    valid_combinations.append(
    sorted(combo))for combo in all_combos_less_than_or_equal_target_count
    if len(combo) == 4 and sorted(combo) not in valid_combinations
]

for combo in valid_combinations:
    print(combo)

