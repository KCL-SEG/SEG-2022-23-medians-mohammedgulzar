"""Median calculator."""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = sorted([float(value) for value in input().split(",")])
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        if len(numbers) % 2 == 0:
            upper_median = numbers[len(numbers) // 2]
            lower_median = numbers[(len(numbers) // 2) - 1]
            median = (upper_median + lower_median) / 2
            print(f"Median value is {median}")
        else:
            print(f"Median value is {numbers[len(numbers) // 2]}")
        break
