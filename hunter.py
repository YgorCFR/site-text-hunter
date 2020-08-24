
import time
import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import json
import os
import re
import pandas as pd
from scrapy.utils.project import get_project_settings
from scrapy import signals
from scrapy.signalmanager import dispatcher
import logging
from scrapy.utils.log import configure_logging
import scrapy.crawler as crawler


configure_logging(install_root_handler=True)
logging.disable(50)  # CRITICAL = 50



# # your spider
class MySpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = [''' ADD THE DOMAIN OF THE SITE HERE ''']
    start_urls = [''' ADD THE URL OF THE SITE HERE ''']
    
    def parse(self, response):
        dic = {}
        #Extracting the content using css selectors
        dic["response"] = response.text
        yield dic


def spider_results():
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess()

    process.crawl(MySpider)

    process.start() # the script will block here until the crawling is finished
    return results


# THE MAIN METHOD THAT ALLOWS YOU TO ITERATE THROUGHT THE URL'S
if __name__ == '__main__':
        res = spider_results()
        for b in res:
            soup = BeautifulSoup(str(b["response"]), features='lxml')
            texto = ''
            # CHANGE THE STYLE ATTRIBUTES HERE, YOU NEED TO INSPECT THE SITE THAT YOU WANT TO ANALYSE
            conteudo_do_site = soup.findAll('div', {'class': 'longText'})
            for conteudo in conteudo_do_site:
                texto = texto + str(conteudo)
            texto_bs = BeautifulSoup(texto, features="lxml")
            texto_bs_refinado = re.sub('\s+', ' ', texto_bs.get_text())
            print(texto_bs_refinado)

