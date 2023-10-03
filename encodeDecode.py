def decode(s):
    count = 0
    ret = ""
    for c in s:
        if c.isdigit():
            count = count*10 + ord(c) - ord('0')
        else:
            ret += c*count
            count = 0
    return ret


def encode(s):
    count = 1
    i = 0
    ret = ""

    while  i < len(s):
        if i + 1 < len(s) and s[i] == s[i+1]:
            count +=1
        else:
            ret += str(count) + s[i]
            count = 1 
        i+=1
    return ret

            




if __name__ == '__main__':
    s = "3e4f2e"
    print(decode(s))
    s = "4a1b3c2a"
    print(decode(s))
    d = "aaaabcccaa"
    print("Encode", d, "with",  encode(d))
    d = "eeeffffee"
    print("Encode", d, "with",  encode(d))

