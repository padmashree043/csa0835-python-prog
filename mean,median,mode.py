elements = [16, 18, 27, 16, 23, 21, 19]
total_sum = sum(elements)
count = len(elements)
mean = total_sum / count
sorted_elements = sorted(elements)
if count % 2 == 1:
    median = sorted_elements[count // 2]
else:
    median = (sorted_elements[(count // 2) - 1] + sorted_elements[count // 2]) / 2
frequency = {}
for num in elements:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

mode = max(frequency, key=frequency.get)
print(f"Mean = {mean}")
print(f"Median = {median}")
print(f"Mode = {mode}")
