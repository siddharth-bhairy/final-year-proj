import requests
from bs4 import BeautifulSoup
import pandas as pd
import random



def getRandomProxy():
    proxy={
        "http": f"http://Kh072ICB0vRFuRg9:wifi;;@proxy.soax.com{9000 + random.randint(0,299)}",
        "https": f"http://Kh072ICB0vRFuRg9:wifi;;@proxy.soax.com{9000 +random.randint(0,299)}",
        
    }
    
    resp=requests.get("http://checker.soax.com/api/ipinfo",proxies=proxy)
    print(resp.text)


reviewlist=[]
getRandomProxy()