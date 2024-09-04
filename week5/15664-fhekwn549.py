def back_tracking(idx, temp):  
    if len(temp) == M:  
        if not tuple(temp) in result:  
            print(*temp)  
            result.add(tuple(temp))  
    for i in range(idx, N):  
        temp.append(nums[i])  
        back_tracking(i+1, temp)  
        temp.pop()  

N, M = map(int, input().split())  
nums = [*map(int, input().split())]  
nums.sort()  

result = set()  
back_tracking(0, [])
