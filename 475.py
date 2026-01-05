numbers = list(map(int, input().split()))
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
duplicates.sort()
for num in duplicates:
    print(num, end=" ")