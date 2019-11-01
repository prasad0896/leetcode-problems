def romanToInt(s):
    dic = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    num = 0
    for i in range(len(s)-1):
        if dic[s[i]] < dic[s[i+1]]:
            num -= dic[s[i]]
        else:
            num += dic[s[i]]
    num = num + dic[s[-1]]
    print(num)
    return num
romanToInt('VIIII')