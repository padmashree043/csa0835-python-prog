grade=input("enter the grade of the employee:").strip().upper()
salary=float(input("enter the employee salary:"))
bonus=0
if grade=='A':
    bonus=salary*0.05
elif grade=='B':
    bonus=salary*0.10
if salary<10000:
    bonus+=salary*0.02
total_amount=salary+bonus
print(f"salary={salary}")
print(f"bonus={bonus}")
print(f"total to be paid:{total_amount}")
