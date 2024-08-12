# 1475
nums = [0]*9

num = input("")
temp = 1
if int(num) > 1000000:
    temp = 0


for i in num:
    if i == '6' or i == '9':
        nums[6] += 1
    else:
        nums[int(i)] += 1

nums[6] = (nums[6] + 1) // 2

if temp == 1:
    print(max(nums))
    
    
# 10808
count = [0]*26
word = input("")

for k in word:
    count[ord(k) - ord('a')] += 1

result = ''
for k in count:
    result = result + str(k) + " "
if (len(word) <= 100) and word.islower():
    print(result)