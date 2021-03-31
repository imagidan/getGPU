#used to get pages
import requests

#BeautifulSoup for transforming the page into some nice html
from bs4 import BeautifulSoup as bs

#my favorite GPU
favGPU = "https://www.bestbuy.ca/en-ca/product/evga-nvidia-geforce-rtx-3090-xc3-ultra-gaming-24gb-gddr6x-video-card/14967857"

#This item is available and is used for tests
testItem = "https://www.bestbuy.ca/en-ca/product/insignia-insignia-10-ft-charge-cable-for-xbox-one-s-ns-gxboscc18-c/10510645?cmp=seo-10510645&cmp=knc-s-71700000065688771&gclsrc=ds&gclsrc=ds"

#class for unavailable items
disabledClass = ".disabled_LqxUL"

#Some headers are needed to look like its a human, at least for best buy
headerDictionary = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

#count to see how much time has gone since GPU was first available
count = 0

while(1):
    
    #get page (not in nice html yet)
    uglyPage = requests.get(favGPU,headers=headerDictionary)
    
    #transform ugly page to html page
    page = bs(getPage.text, 'lxml')
    
    #get cart html. [blablabla] if not available, [] if available
    cart = page.select(disabledClass)
    
    #check if cart is not disabled ( [] )
    if cart == []:
        
        #add 1 to count to show the time that has gone by
        count += 1
        
        #print message with count
        print("OMG GPUs ARE BACK! GO GO GO! {}".format(count))
        
    else:
        
        #reset count
        count = 0
