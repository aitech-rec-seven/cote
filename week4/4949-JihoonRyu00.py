import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    results = []
    stack = []

    for string in data:
        
        if string == '.':
            break
        
        stack.clear()
        for s in string:
            
            if s == '(' or s == '[':
                stack.append(s)

            elif s == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    results.append('no')
                    break
                
            elif s == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    results.append('no')
                    break
                
            elif s == '.':
                if stack:
                    results.append('no')
                    break
                else:
                    results.append('yes')
                    break
            
            else:
                continue
    
    print("\n".join(results))

main()

# input 크기: M*N(=len(data)*len(string))
# 시간복잡도: O(M*N)
# 공간복잡도: O(M*N)