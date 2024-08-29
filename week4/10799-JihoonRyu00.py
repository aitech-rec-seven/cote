import sys
input = sys.stdin.read

def main():
    data = input()
    # stack = []
    remainder = 0
    pieces =0
    for i in range(len(data)):
        if data[i] == '(':
            remainder += 1
        elif data[i] == ')':
            remainder -= 1
            if data[i-1] == '(':
                pieces += remainder
            elif data[i-1] == ')':    
                pieces += 1
    
    print(pieces)

main()

# input 크기: N(=len(data))
# 시간복잡도: O(N)
# 공간복잡도: O(N)