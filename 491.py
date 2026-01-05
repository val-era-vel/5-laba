n = input()
max_num = -1
for i in range(len(n)):
    current_num = int(n[:i] + n[i+1:])
    if current_num > max_num:
        max_num = current_num
print(max_num)

