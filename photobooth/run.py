import urllib.request
from gopro.urls import *

class Hero:
    
    def __init__(self):
        self.test = "1"
    
    def beep(self, on):
        if on:
            self.http_get(LOCATE_ON)
        else:
            self.http_get(LOCATE_OFF)
            
    def http_get(self, url):
        return urllib.request.urlopen(url).read()
    
    
cam = Hero()
cam.beep(True)