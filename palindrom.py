s = "aaa"
n = len(s)
count = 0
for center in range(n):
    left = center
    right = center
    while left >= 0 and right < n and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
for center in range(n - 1):
    left = center
    right = center + 1
    while left >= 0 and right < n and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1

print(count)
