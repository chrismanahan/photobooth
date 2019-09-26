import urllib.request
from urls import *

def test():
    print("test")

class Hero:
    
    def __init__():
        self.test = "1"
    
    def beep(on):
        if on:
            http_get(LOCATE_ON)
        else:
            http_get(LOCATE_OFF)
            
    def http_get(url):
        return urllib.request.urlopen(url).read()