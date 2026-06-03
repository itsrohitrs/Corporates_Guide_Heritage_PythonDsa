student_name = "Rohit Singh"
student_id_input = "1042"
cgpa_input = "8.50"
department = "CSE"
is_active = True

student_id = int(student_id_input)
cgpa = float(cgpa_input)

print("\n===== STUDENT PROFILE =====")

print(f"Name       : {student_name}")
print(f"ID         : {student_id:06d}")
print(f"Department : {department}")
print(f"CGPA       : {cgpa:.2f}")
print(f"Active     : {is_active}")

print("\n===== DATA TYPES =====")

print(type(student_name))
print(type(student_id))
print(type(cgpa))
print(type(department))
print(type(is_active))