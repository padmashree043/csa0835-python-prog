n=input("enter a string:")
letters=0
digits=0
for char in n:
    if char.isalpha():
        letters+=1
    elif char.isdigit():
        digits+=1
print("letter",letters)
print("digit",digits)
