def isplaindrome(x):
    st = str(x)
    i = 0
    j = len(st)-1
    while i<j:
        if st[i] != st[j]:
            print("Not-palindrome")
            return False
        i += 1
        j -= 1
    print("is palindrome")
    return True

isplaindrome(121)