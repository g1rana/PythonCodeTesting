def subStringSearch(s , t):
    '''
    use Robin-Kharp algorith to use rolling hash to find first occurance of sub string s in txt
    '''
    kbase = 26
    power_s = 1
    mod = 10**9 + 9 #larget prim number
    hash_s = 0
    hash_t = 0
    for i in range (len(s)):
        #hash_s = (hash_s*kbase + ord(s[i]) - ord('a'))%mod
        #hash_t = (hash_t*kbase + ord(t[i]) - ord('a'))%mod
        if i > 0:
            power_s = kbase*power_s
        hash_s = (hash_s + (ord(s[i]) - ord('a'))*power_s)%mod
        hash_t = (hash_t + (ord(t[i]) - ord('a'))*power_s)%mod

    print("hash_s", hash_s, "hash_t", hash_t, "power_s", power_s, "i", i)
    #Start from fist sub string window end points
    for j in range(len(s), len(t)):
        if hash_s == hash_t and s == t[j-len(s):j]:
            print("sub string", s, "matched with text",t, "at", j - len(s))
            return j - len(s)
        #build rolling hash
        print("old roll hash_t", hash_t, "sub", s, "target sub", t[j-len(s):j])
        #hash_t = hash_t - (ord(t[j-len(s)]) - ord('a'))*power_s
        #hash_t = (hash_t*kbase + ord(t[j]) - ord('a'))%mod
        hash_t = ((hash_t - ord(t[j - len(s)]))/kbase)
        hash_t = (hash_t + (ord(t[j]) -ord('a'))*power_s)%mod

        print("new roll hash_t", hash_t)

    
    #Tries to match s and t[len(t) - len(s) : len(t)]
    if hash_t == hash_s and s == t[len(t) - len(s) : ]:
        print("Step2:sub string", s, "matched with text",t, "at", (len(t) - len(s)))
        return len(t) - len(s)
    print("No match found for" , s , "sub string into", t)
    return -1




if __name__ == '__main__':
    s = "CCA"
    txt = "GACGCCA"
    subStringSearch(s,txt)


