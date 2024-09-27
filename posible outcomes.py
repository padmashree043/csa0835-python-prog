num = input("Enter 3 digits: ")
digits = list(num)
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k:
                print(digits[i] + digits[j] + digits[k])
