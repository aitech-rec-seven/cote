n = input()
count = [0] * 10

for num in n:
    if num == '6' or num == '9':
        count[6] += 1
    else:
        count[int(num)] += 1

count[6] = count[6] // 2 + count[6] % 2

print(max(count))