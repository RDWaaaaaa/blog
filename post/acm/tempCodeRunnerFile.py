a, b = input().split()
flag = 0
ans = ''
if a.isdigit():
    ans += a
else:
    ans += '?'
    flag = 1
ans += ' + '
if b.isdigit():
    ans += b    
else:
    ans += '?'
    flag = 1
ans += ' = '
if flag == 1:
    ans += '?'
else:
    ans += str(int(a) + int(b))
print(ans)