import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime
import pandas as pd
# import json
# import numpy as np
# import urllib


class KendalSpider(scrapy.Spider):
    name = "kendal"
    start_urls = [
        "https://corona.kendalkab.go.id/"
    ]

    custom_settings = {
        # 'ITEM_PIPELINES': {'DOWNLOAD_DELAY': 1},
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'kendal.csv'
    }

    months = dict(January='01', February='02', March='03', April='04', May='05', June='06',
                  July='07', August='08', September='09', October='10', November='11', December='12')

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kecamatan'
        user_pic = 'Alfie Qashwa'
        crawl_date = response.xpath(
            '/html/body/div[1]/section[2]/div[1]/div/div/div[1]/p/text()')[4].re(r', (\w+) (\w+) (\w+)')
        day = crawl_date[0]
        month = crawl_date[1]
        year = crawl_date[2]
        date_update = year + '-' + self.months[month] + '-' + day
        provinsi = 'Jawa Tengah'
        kabkot = 'Kendal'
        kecamatan = response.xpath(
            '//*[@id="example1"]/tbody/tr/td[2]/text()').getall()
        total_odp = response.xpath(
            '//*[@id="example1"]/tbody/tr/td[5]/text()').getall()
        total_pdp = response.xpath(
            '//*[@id="example1"]/tbody/tr/td[6]/text()').getall()
        total_positif = response.xpath(
            '//*[@id="example1"]/tbody/tr/td[7]/text()').getall()
        odr_total = response.xpath(
            '//*[@id="example1"]/tbody/tr/td[4]/text()').getall()
        source_link = 'https://corona.kendalkab.go.id/'

        for q in range(len(kecamatan)):
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan[q].capitalize().strip(),
                'kelurahan': '',
                'alamat': '',
                'total_odp': total_odp[q].strip(),
                'total_pdp': total_pdp[q].strip(),
                'total_positif': total_positif[q].strip(),
                'positif_sembuh': '',
                'positif_dirawat': '',
                'positif_isolasi': '',
                'positif_meninggal': '',
                'total_otg': '',
                'odr_total': odr_total[q].strip(),
                'total_pp': '',
                'total_ppdt': '',
                'source_link': source_link,
            }


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(KendalSpider)
    process.start()
