import scrapy
from oryx_scrape.data_processing import process_data
from oryx_scrape import spiders_settings

class Spider(scrapy.Spider):
    name = spiders_settings.spider_ukraine
    allowed_domains = [spiders_settings.oryx_domain]
    start_urls = [spiders_settings.oryx_url_ukraine_losses]


    def parse(self, response):

        tanks = response.xpath('//h3[./*[@class="mw-headline" and @id="Pistols" and contains(text(), "Tanks")]]/text()').get()
        afv = response.xpath('//h3[./*[@class="mw-headline" and @id="Pistols" and contains(text(), "Armoured Fighting Vehicles")]]/text()').get()
        ifv = response.xpath('//h3[./*[@class="mw-headline" and @id="Pistols" and contains(text(), "Infantry Fighting Vehicles")]]/text()').get()
        apc = response.xpath('//h3[./*[@class="mw-headline" and @id="Pistols" and contains(text(), "Armoured Personnel Carriers")]]/text()').get()
        imv = response.xpath('//h3[./*[@class="mw-headline" and @id="Pistols" and contains(text(), "Infantry Mobility Vehicles")]]/text()').get()

        tanks_processed = process_data(tanks) # tanks
        afv_processed = process_data(afv) # armoured fighting vehicle
        ifv_processed = process_data(ifv) # infantry fighting vehicle
        apc_processed = process_data(apc) # armoured personnel carrier
        imv_processed = process_data(imv) # infantry mobility vehicle

        total_casualties = {
            'tank': tanks_processed,
            'afv': afv_processed,
            'ifv': ifv_processed,
            'apc': apc_processed,
            'imv': imv_processed,
            }


        yield total_casualties
