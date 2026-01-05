numbers = input().split()
count = 0
for num in numbers:
    if int(num) > 0:
        count += 1
print(count)

