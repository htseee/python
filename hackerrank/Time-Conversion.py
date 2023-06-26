time = input()
s = time.split(':')
AM = s[2][2:]
s[2] = s[2][:2]
if AM == 'AM':
    if s[0] == '12':
        s[0] = '00'
    print(s[0], ':', s[1], ':', s[2], sep='')
else:
    if s[0] != '12':
        s[0] = str(int(s[0]) + 12)
    print(s[0], ':', s[1], ':', s[2], sep='')