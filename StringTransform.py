
def isDigit(c):
    if ord(c) - ord('0') >= 0 and ord(c) - ord('0') <= 9:
        return True
    return False

def miniMumTransformOper(s):
    r,w = 0,0
    arr = list(s)
    op = 0
    while r < len(arr):
        print("r",r, "s[r]",arr[r], "w",w ,"isDisgi",isDigit(arr[r]))
        if not isDigit(arr[r]):
            if arr[r] != arr[w]:
                arr[w] = arr[r]
                op +=1
            w +=1
        r +=1
    return "".join(arr), op



if __name__ == "__main__":
    s = "a0bb12p"
    t,op = miniMumTransformOper(s)
    print("s",s,"->",t,"num operation",op)

