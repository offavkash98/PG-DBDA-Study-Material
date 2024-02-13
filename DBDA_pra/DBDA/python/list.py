subs = int(input("how many subject"))
all_sub_marks = []

for i in range(subs):
    marks = float(input("enter marks:"))
    all_sub_marks.append(marks)
print(all_sub_marks )

higest_marks = max(all_sub_marks)
lowest_marks = min(all_sub_marks)

print("you got higest marks of",higest_marks)
print("you got higest marks of",lowest_marks)

total_marks = sum(all_sub_marks)
avg_marks = total_marks/subs
print("you got average marks of",avg_marks)
