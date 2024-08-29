result = []
while True:
    in_list = []
    sentence = input("")
    balance = 1
    if sentence == ".":
        break
    else:
        each = list(sentence)
        for i in each:
            if i in ['(', '[']:
                in_list.append(i)
            elif i==')' and len(in_list)!=0:
                if in_list[-1]=='(':
                    del in_list[-1]
                else:
                    balance = 0
                    break
            elif i==']' and len(in_list)!=0:
                if in_list[-1]=='[':
                    del in_list[-1]
                else:
                    balance = 0
                    break
            elif i in [')', ']']:
                balance = 0
                break
        if balance == 1 and len(in_list) == 0:
            result.append('yes')
        else:
            result.append('no')                
                
print('\n'.join(result))           
