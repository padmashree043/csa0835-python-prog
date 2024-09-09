count_lowercase = 0
count_uppercase = 0
count_numbers = 0
while True:
    char = input("Enter any character: ")
    if char == '*':
        break
    if char.islower():
        count_lowercase += 1
    elif char.isupper():
        count_uppercase += 1
    elif char.isdigit():
        count_numbers += 1
print("Total count of lower case:", count_lowercase)
print("Total count of upper case:", count_uppercase)
print("Total count of numbers:", count_numbers)
