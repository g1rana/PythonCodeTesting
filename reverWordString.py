def reverWordString(text):
    wordList = text.split(" ")
    sz = len(wordList)
    for i in range(sz/2):
        wordList[i] , wordList[sz-1-i] =  wordList[sz-1-i],wordList[i]

    return ' '.join(wordList)

mDict = ["0","1","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
def phoneMenonics(text):
    result = []
    partial = ""
    phoneMenonicsHelper(text,0, partial, result)
    return result

def phoneMenonicsHelper(txt, digit, partial, result):
    #base case
    if digit == len(txt):
        #means cover all digits save partial into result then
        result.append(partial)
        return 
    #non-base case:
    i = ord(txt[digit]) - ord('0')
    for c in mDict[i]:
        phoneMenonicsHelper(txt,digit+1 , partial+ c, result)
    return


if __name__ == '__main__':

     s = "greeks quiz practice code"
     print(reverWordString(s))
     s = "123"
     print("for phone:",s)
     print(phoneMenonics(s))
     s = "234"
     print("for phone:",s)
     print(phoneMenonics(s))

