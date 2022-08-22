import urllib
from urllib.request import urlopen

def connectivity():
    
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    
    except urllib.error.URLError as Error:
        print(Error)
        return False
    
    
if connectivity():
    print("URL is up!")
else:
    print("Couldn't reach it. Could you please check back later?")
