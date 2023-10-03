'''
Get list of valid IP address from given number string

'''
def getValidIPaddress(IPs):
    #first subIps
    i = 1
    result = []
    while i < len(IPs) and i < 4:
        firstIps = IPs[0:i]
        if validSub(firstIps):
            j = 1
            while i+j < len(IPs) and j < 4:
                secondIps = IPs[i:i+j]
                if validSub(secondIps):
                    k = 1
                    while i+j+k < len(IPs) and  k <4:
                        thirdIps = IPs[i+j: i+j+k]
                        fourthIps = IPs[i+j+k:]
                        if validSub(thirdIps) and validSub(fourthIps):
                           result.append(firstIps + "." + secondIps + "." + thirdIps + "." + fourthIps)
                        k+=1
                j+=1
        i+=1
    return result

                        

def validSub(s):
    if len(s) > 3:
        return False
    #"00" , "01", "000" are not valid but "0" is valid
    if s[0] == "0" and len(s) > 1:
        return False
    if int(s) > 255:
        return False

    return True

if __name__ == '__main__':
    ip = "19216811"
    print(getValidIPaddress(ip))

