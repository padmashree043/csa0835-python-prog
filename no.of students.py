total_users = int(input("Enter Total Users: "))
staff_users = int(input("Enter Staff Users: "))
if total_users < 0 or staff_users < 0:
    print("Invalid input: Total and Staff Users must be non-negative.")
elif staff_users > total_users:
    print("Invalid input: Staff users cannot be more than total users.")
else:
    non_teaching_staff = staff_users // 3
    student_users = total_users - staff_users - non_teaching_staff
    if student_users >= 0:
        print(f"Student Users: {student_users}")
    else:
        print("Invalid configuration: More staff users than total users.")
