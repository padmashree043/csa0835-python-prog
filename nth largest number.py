numbers = [14, 67, 48, 23, 5, 62]
N = 4
sorted_numbers = sorted(numbers, reverse=True)
nth_largest = sorted_numbers[N - 1]
print(f"{N}th Largest number: {nth_largest}")
