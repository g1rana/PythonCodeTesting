import urllib2
import collections
import re
def parseLogFile(url):
    file = urllib2.urlopen(url)
    target = [ line  for line in file if "Failed password" in line]
    d = collections.defaultdict(int)
    for line in target:
        pattern = r'(?:\d{1,3}\.)+(?:\d{1,3})'
        d[re.search(pattern,line).group()] += 1
    
    r = list(d.items())
    r.sort(key = lambda x: x[1], reverse=True)
    print(r)
    

if __name__ == "__main__":
    parseLogFile("http://bholt.org/ssh/short.txt")
