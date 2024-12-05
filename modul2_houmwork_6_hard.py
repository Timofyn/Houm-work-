number_1 = []
n = int(input("Введите число "))

for i in range(1, n):
    for k in range(1, i):
        if n % (k + i) == 0:
            number_1.append([i,k])

print(number_1)
