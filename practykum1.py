grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = list(students)
print(list_students)
arithmetic_mean = [(sum(grades[0]) / len(grades[0])),(sum(grades[1]) / len(grades[1])),
(sum(grades[2]) / len(grades[2])),(sum(grades[3]) / len(grades[3])),(sum(grades[4]) / len(grades[4]))]
print(arithmetic_mean)
otmetki = {list_students[4] : arithmetic_mean[0], list_students[1] : arithmetic_mean[1],
           list_students[0] : arithmetic_mean[2],list_students[3] : arithmetic_mean[3],
           list_students[2] : arithmetic_mean[4] }
sorted(otmetki)
print(otmetki)