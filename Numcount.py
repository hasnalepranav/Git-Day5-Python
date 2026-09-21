num = 1234
count = 0

for i in range(num):
    if num > 0:
        num = num // 10
        count += 1
    else:
        break

print(count)