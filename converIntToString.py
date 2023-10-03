def converIntToString(num):
        is_negative = False
        if num < 0:
            is_negative = True
            num = -num
        
        res = ""
        while num:
            print(num, "res", res)
            res += chr(ord('0') + num%10)
            num /=10

        if is_negative:
            res +='-'
        return res[::-1]

def converStringToInt(number):
    if len(number) == 0:
        return ""
    is_negative = False
    if number[0] == '-':
        is_negative = True
        number = number[1:]
    ret = 0
    for n in number:
        ret = ret*10 + ord(n) - ord('0')
    if is_negative:
        ret = -ret

    return ret

def baseNumStrToDecimal(num,base):
    if len(num) == 0:
        return num
    is_negative = False
    if num[0] == '-':
        is_negative = True
        num = num[1:]
    ret = 0
    for c in num:
        ret *= base
        if isdigit(c):
            diff = ord(c) - ord('0')
        else:
            diff = ord(c) - ord('A') + 10
        ret += diff

    if is_negative:
        ret = -ret
    return ret



if __name__ == '__main__':
    #t = converIntToString(-1234)
    #print(type(t),t)
    #t = baseNumStrToDecimal("-4567") 
    #print(type(t),t)
    t = baseNumStrToDecimal("306",7)
    print(type(t),t)





