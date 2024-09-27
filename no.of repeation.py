a = "abcd"
b = "cdabcdab"
repeated_a = a
count = 1 
while len(repeated_a) < len(b) or b not in repeated_a:
    repeated_a += a
    count += 1
    if len(repeated_a) > len(b) + len(a):
        print(-1)
        break
else:
    print(count)
