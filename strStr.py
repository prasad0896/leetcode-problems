def strStr(haystack,needle):
    if not len(needle):
        return 0
    for i in range(0,len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            print(i)
            return i
    print(-1)
    return -1

strStr("hello","ll")
