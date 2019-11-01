def reverse(x):
    #perform overflow checks
    if x < 0:
        x = -1 * x
        st = str(x)
        #print(int(st[::-1])*-1)
        reverse = int(st[::-1])*-1
    else:
        st = str(x)
        #print(int(st[::-1]))
        reverse = int(st[::-1])
        
    if reverse < int(-2**31):
        #print(0)
        return 0
    elif reverse >= int(2**31):
        #print(0)
        return 0
    else:
        return reverse

reverse(2**30)