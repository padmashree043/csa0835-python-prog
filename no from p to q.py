P = int(input("Enter P: "))
Q = int(input("Enter Q: "))
R = str(input("Enter R: "))
valid_numbers = []
for number in range(P, Q + 1):
    if R not in str(number):
        valid_numbers.append(number)
print("Numbers are =", ", ".join(map(str, valid_numbers)))
