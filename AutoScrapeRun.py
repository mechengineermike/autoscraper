#!/usr/bin/env python3
import os

from autoscraper import AutoScraper
    #python3 -m pip install autoscraper
    #sudo chmod a+rwxX /home/pi/Desktop/scraper/
    #sudo python3 /home/pi/Desktop/scraper/AutoScrapeRun.py

data_dir = '/home/pi/Desktop/scraper/'
scrapeRecord = os.path.join(data_dir,'Results.txt') # location to save records of file send attempts for troubleshooting

scraperitemFavorites = AutoScraper()
scrapershopSales= AutoScraper()
scraperlastSale= AutoScraper()
scraperbestSeller= AutoScraper()
scraperstars= AutoScraper()
scraperitemReviews= AutoScraper()
scrapershopReviews= AutoScraper()
scrapershopAge= AutoScraper()
#scrapertotalItems= AutoScraper()
scraperprice= AutoScraper()

scrapershopSales.load('scrapershopSales')
scraperlastSale.load('scraperlastSale')
scraperbestSeller.load('scraperbestSeller')
scraperstars.load('scraperstars')
scraperitemReviews.load('scraperitemReviews')
scrapershopReviews.load('scrapershopReviews')
scrapershopAge.load('scrapershopAge')
#scrapertotalItems.load('scrapertotalItems')
scraperprice.load('scraperprice')


keyword1 = '3d'
keyword2 = 'print'
#keyword3 = ' '
pageNum  = 1 #search results page number

urlMainSearch ='https://www.etsy.com/search?q='
urlMainSearch =urlMainSearch+keyword1
urlMainSearch =urlMainSearch+'+'+keyword2
#urlMainSearch =urlMainSearch+'+'+keyword3
urlMainSearch =urlMainSearch+'&ref=pagination&page='
urlMainSearch =urlMainSearch+str(pageNum)

urlMainSearch ='https://www.etsy.com/search?q=3d+printing&ref=pagination&page=2'

#'https://www.etsy.com/search?q=3d+printing'
         #'https://www.etsy.com/search?q=3d+printing&ref=pagination&page=2'

print(urlMainSearch)
scraperMain = AutoScraper()
scraperMain.load('etsyMain')
print('here1')
resultsMain = scraperMain.get_result_similar(urlMainSearch, contain_sibling_leaves=True)#, keep_order=True) group_by_alias=True)
#attr_fuzz_ratio=0.8)
print(resultsMain)
loop =1
print('here2')
for listingUrl in resultsMain:
    print('loop#' +loop)
    loop = loop+1
    outF = open(scrapeRecord,"a")#, "a") #a for append.

    scraped= scraperitemFavorites.get_result_similar(listingUrl)#,grouped=True group_by_alias=True)#,keep_order=True)# contain_sibling_leaves=True)
    if len(scraped)==0: #if not scraped:
        saveMe='0'
    else:
        saveMe=';'.join([str(elem) for elem in scraped])
        saveMe=saveMe.replace('\n','')
    print(saveMe)
    outF.write(saveMe)
    outF.write(';')
    
    scraped= scrapershopSales.get_result_similar(listingUrl)#,grouped=True group_by_alias=True)#,keep_order=True)# contain_sibling_leaves=True)
    if len(scraped)==0:
        saveMe='0'
    else:
        saveMe=';'.join([str(elem) for elem in scraped])
        saveMe=saveMe.replace('\n','')
    print(saveMe)
    outF.write(saveMe)
    outF.write(';')
    
    scraped= scraperlastSale.get_result_similar(listingUrl)#,grouped=True group_by_alias=True)#,keep_order=True)# contain_sibling_leaves=True)
    if len(scraped)==0:
        saveMe='0'
    else:
        saveMe=str(scraped[0])
        #saveMe=';'.join([str(elem) for elem in scraped])
        saveMe=saveMe.replace('\n','')
    print(saveMe)
    outF.write(saveMe)
    outF.write(';')
    
    scraped= scraperitemReviews.get_result_similar(listingUrl)#,grouped=True group_by_alias=True)#,keep_order=True)# contain_sibling_leaves=True)
    if len(scraped)==0:
        saveMe='0'
    else:
        if str(scraped[0]) != '60' and str(scraped[0]) != '209':
            saveMe=str(scraped[0])
        else:
            saveMe='0'
    print(saveMe)
    outF.write(saveMe)
    outF.write(';')
    
    scraped= scrapershopReviews.get_result_similar(listingUrl)#,grouped=True group_by_alias=True)#,keep_order=True)# contain_sibling_leaves=True)
    if len(scraped)==0:
        saveMe='0'
    else:
        print("shop reviews")
        print(scraped)
        if len(scraped)>=2:
            if str(scraped[1]) != '286' and str(scraped[0]) != '209':
               saveMe=str(scraped[1])
            else:
                saveMe='0'
        
    print(saveMe)
    outF.write(saveMe)
    outF.write(';')
    
    scraped= scrapershopAge.get_result_similar(listingUrl)#,grouped=True group_by_alias=True)#,keep_order=True)# contain_sibling_leaves=True)
    if len(scraped)==0:
        saveMe='0;0'#because its replacing 2 items that wouldve been found
    else:
        del scraped[0]
        saveMe=';'.join([str(elem) for elem in scraped])
        saveMe=saveMe.replace('\n','')
    print(saveMe)
    outF.write(saveMe)
    outF.write(';')
            
#             scraped= scrapertotalItems.get_result_similar(listingUrl)#,grouped=True group_by_alias=True)#,keep_order=True)# contain_sibling_leaves=True)
#             if not scraped:
#                 saveMe ='0'
#             else:
#                 saveMe=';'.join([str(elem) for elem in scraped])
#                 saveMe=saveMe.replace('See all ','')
#                 saveMe=saveMe.replace('\n','')
#             print(saveMe)
#             outF.write(saveMe)
#             outF.write(';')
    
    scraped= scraperprice.get_result_similar(listingUrl)#,grouped=True group_by_alias=True)#,keep_order=True)# contain_sibling_leaves=True)
    if len(scraped)==0:
        saveMe = '0'
    else:
        saveMe = str(scraped[0])
        saveMe=saveMe.replace('\n','')
        saveMe=saveMe.replace(' ','')
        saveMe=saveMe.replace('Price:','')
    print(saveMe)
    #saveMe=';'.join([str(elem) for elem in scraped])
    outF.write(saveMe)
    outF.write(';')
    
    scraped= scraperstars.get_result_similar(listingUrl)#,grouped=True group_by_alias=True)#,keep_order=True)# contain_sibling_leaves=True)
    if len(scraped)==0:
       saveMe='0'
    else:
        saveMe = str(scraped[0])
        saveMe=saveMe.replace(' out of 5 stars','')
        saveMe=saveMe.replace('\n','')
    print(saveMe)
    outF.write(saveMe)
    outF.write(';')
    
    scraped= scraperbestSeller.get_result_similar(listingUrl)#,grouped=True group_by_alias=True)#,keep_order=True)# contain_sibling_leaves=True)
    if len(scraped)==0:
        saveMe='0'
    else:
        saveMe=';'.join([str(elem) for elem in scraped])
        saveMe=saveMe.replace('\n','')
    print(saveMe)
    outF.write(saveMe)
    outF.write(';')
    
    

    outF.write(listingUrl)
    outF.write('\n')
    outF.close()
        
#     print('complete!')
# except:
#     print('Error...!')



