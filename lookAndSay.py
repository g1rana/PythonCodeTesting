def lookAndSay(n):
    s = "1"
    for i in range(n):
        print("it:",i)
        s = nextNumber(s)
    return s

def nextNumber(s):
    ret = ""
    i = 0
    while(i < len(s)):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            count +=1
            i +=1
        ret += str(count) + s[i]
        i +=1
        print("ret", ret)
    return ret



if __name__ == '__main__':
    n = 4
    print("num :",n)
    print("LookAndSay:", lookAndSay(n))

