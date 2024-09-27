num = 5
bits = 0
temp = num
while temp > 0:
    bits += 1
    temp //= 2
mask = (1 << bits) - 1
complement = num ^ mask
print(complement)
