a = 12
b = 19
def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True  
    return False
composite_numbers = []
for num in range(a, b+1):
    if is_composite(num):
        composite_numbers.append(num)
print("Composite numbers between", a, "and", b, "are:", ', '.join(map(str, composite_numbers)))
