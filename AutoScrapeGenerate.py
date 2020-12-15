#!/usr/bin/env python3
import os


#Etsy scraper

from autoscraper import AutoScraper

print('started scraping...')

data_dir = '/home/pi/Desktop/scraper/'
#scrapeRecord = os.path.join(data_dir,'scrapeRecord.csv') # location to save records of file send attempts for troubleshooting

urlMain = 'https://www.etsy.com/search?q=cosplay%20fire'
urlex = 'https://www.etsy.com/listing/674681682/fire-ice-cosplay-light-up-led-wearable?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=cosplay+fire&ref=sr_gallery-1-2&organic_search_click=1&frs=1&col=1'
wanted_list = [urlex] #This is the most simple search type, just a one page input

MainLink = [('https://www.etsy.com/search?q=cosplay%20fire',['https://www.etsy.com/listing/674681682/fire-ice-cosplay-light-up-led-wearable?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=cosplay+fire&ref=sr_gallery-1-2&organic_search_click=1&frs=1&col=1']),]
scraperMain = AutoScraper() #define a new scraper object
for targetUrl, wanted_list in MainLink:
    scraperMain.build(url=targetUrl, wanted_list=wanted_list)
    #scraperMain.build(urlMain, wanted_list) #build the contents of that scraper
scraperMain.save('etsyMain') #Saves this particular build of the scraper! (note, this is a local file, you can load it w/o having to regenerate very time!)


#Build a new batch of features to collect. Best to collect them seperately from each other so they dont cross wires!
itemFavorites = [('https://www.etsy.com/listing/674681682/fire-ice-cosplay-light-up-led-wearable?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=cosplay+fire&ref=sr_gallery-1-3&organic_search_click=1&frs=1',['1525 favorites']),]
scraperitemFavorites = AutoScraper()
for targetUrl, wanted_list in itemFavorites:
   scraperitemFavorites.build(url=targetUrl, wanted_list=wanted_list)#, update=True)# grouped =True)
scraperitemFavorites.save('scraperitemFavorites')
   
shopSales = [('https://www.etsy.com/listing/674681682/fire-ice-cosplay-light-up-led-wearable?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=cosplay+fire&ref=sr_gallery-1-3&organic_search_click=1&frs=1',['1,694 sales']),]
scrapershopSales= AutoScraper()
for targetUrl, wanted_list in shopSales:
   scrapershopSales.build(url=targetUrl, wanted_list=wanted_list)#, update=True)# grouped =True)
scrapershopSales.save('scrapershopSales')

lastSale = [('https://www.etsy.com/listing/674681682/fire-ice-cosplay-light-up-led-wearable?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=cosplay+fire&ref=sr_gallery-1-3&organic_search_click=1&frs=1',['Listed on Dec 14, 2020']),]
scraperlastSale= AutoScraper()
for targetUrl, wanted_list in lastSale:
   scraperlastSale.build(url=targetUrl, wanted_list=wanted_list)#, update=True)# grouped =True)
scraperlastSale.save('scraperlastSale')   
   
bestSeller = [('https://www.etsy.com/listing/817305340/fire-nation-princess-azula-headpiece?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=cosplay+fire&ref=sr_gallery-1-2&organic_search_click=1&bes=1&col=1',['Bestseller']),]
scraperbestSeller= AutoScraper()
for targetUrl, wanted_list in bestSeller:
   scraperbestSeller.build(url=targetUrl, wanted_list=wanted_list)#, update=True)# grouped =True)
scraperbestSeller.save('scraperbestSeller')   

stars = [('https://www.etsy.com/listing/674681682/fire-ice-cosplay-light-up-led-wearable?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=cosplay+fire&ref=sr_gallery-1-3&organic_search_click=1&frs=1',['5 out of 5 stars']),]
scraperstars= AutoScraper()
for targetUrl, wanted_list in stars:
   scraperstars.build(url=targetUrl, wanted_list=wanted_list)#, update=True)# grouped =True)
scraperstars.save('scraperstars')

itemReviews=[('https://www.etsy.com/listing/674681682/fire-ice-cosplay-light-up-led-wearable?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=cosplay+fire&ref=sr_gallery-1-3&organic_search_click=1&frs=1',['66']),]
scraperitemReviews= AutoScraper()
for targetUrl, wanted_list in itemReviews:
   scraperitemReviews.build(url=targetUrl, wanted_list=wanted_list)#, update=True)# grouped =True)
scraperitemReviews.save('scraperitemReviews')   
   
shopReviews=[('https://www.etsy.com/listing/674681682/fire-ice-cosplay-light-up-led-wearable?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=cosplay+fire&ref=sr_gallery-1-3&organic_search_click=1&frs=1',['333']),]
scrapershopReviews= AutoScraper()
for targetUrl, wanted_list in shopReviews:
   scrapershopReviews.build(url=targetUrl, wanted_list=wanted_list)#, update=True)# grouped =True)
scrapershopReviews.save('scrapershopReviews')

shopAge =[('https://www.etsy.com/listing/674681682/fire-ice-cosplay-light-up-led-wearable?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=cosplay+fire&ref=sr_gallery-1-3&organic_search_click=1&frs=1',['2018']),]
scrapershopAge= AutoScraper()
for targetUrl, wanted_list in shopAge:
   scrapershopAge.build(url=targetUrl, wanted_list=wanted_list)#, update=True)# grouped =True)
scrapershopAge.save('scrapershopAge')
# 
# totalItems =[('https://www.etsy.com/listing/674681682/fire-ice-cosplay-light-up-led-wearable?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=cosplay+fire&ref=sr_gallery-1-3&organic_search_click=1&frs=1',['See all 48 items']),]
# scrapertotalItems= AutoScraper()
# for targetUrl, wanted_list in totalItems:
#    scrapertotalItems.build(url=targetUrl, wanted_list=wanted_list)#, update=True)# grouped =True)
# scrapertotalItems.save('scrapertotalItems')

price = [('https://www.etsy.com/listing/674681682/fire-ice-cosplay-light-up-led-wearable?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=cosplay+fire&ref=sr_gallery-1-3&organic_search_click=1&frs=1',['$35.00+']),]
scraperprice= AutoScraper()
for targetUrl, wanted_list in price:
   scraperprice.build(url=targetUrl, wanted_list=wanted_list)#, update=True)# grouped =True)
scraperprice.save('scraperprice')

#shopLink = 'https://www.etsy.com/shop/RadiantArtifacts?ref=simple-shop-header-name&listing_id=674681682'

print('complete!')
