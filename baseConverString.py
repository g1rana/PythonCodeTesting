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
        if c.isdigit():
            diff = ord(c) - ord('0')
        else:
            diff = ord(c) - ord('A') + 10
        ret += diff

    if is_negative:
        ret = -ret
    return ret

def convDecimalToBaseHelper(d,num,base):
    print("depth:", d, "recv num",num,"base",base,"num%base", num%base, "num/base", num/base)
    if num == 0:
        return ""
    r = convDecimalToBaseHelper(d+1,num/base,base)
    if num % base >= 10:
        return r + chr(ord('A') + (num%base -10)) 
    else:
        return r + chr(ord('0') + num%base)

def convDecimalToBaseString(num,base):
    is_negative = False
    if num < 0:
        is_negative = True
        num = -num
    ret = convDecimalToBaseHelper(0,num,base)
    if is_negative:
        return "-" + ret
    return ret

def SSDecodeID(s):
    ret = 0 
    for c in s:
        ret = ret*26 + ord(c) - ord('A') + 1
    return ret




if __name__ == '__main__':
    #t = converIntToString(-1234)
    #print(type(t),t)
    #t = baseNumStrToDecimal("-4567")
    #print(type(t),t)
    t = baseNumStrToDecimal("-615",7)
    print(type(t),t)
    t = convDecimalToBaseString(t,13)
    print(type(t),t)
    ret = SSDecodeID("ZZ")
    print(type(ret),ret)
    ret = SSDecodeID("ZZ")



