#Skip all non-alphanumeric charater and ignore character casecencitive

def IsTextStringPalindrom(text):
    i = 0
    j = len(text) -1
    while i < j:
        #skip all non-alphanumeric
        while not text[i].isalnum():
            i +=1
        while not text[j].isalnum():
            j -=1
        if text[i].lower() != text[j].lower():
            return False
    return True


if __name__ == '__main__':
    s = "Ray a Ray"
    print("Is string Palindrom:",IsTextStringPalindrom(s)) 
