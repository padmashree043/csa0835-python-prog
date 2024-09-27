nums = [5, 4, 0, 3, 1, 6, 2]
n = len(nums)
visited = [False] * n
longest = 0
for i in range(n):
    if not visited[i]:
        count = 0
        k = i
        while not visited[k]:
            visited[k] = True
            k = nums[k]
            count += 1
        if count > longest:
            longest = count

print(longest)
