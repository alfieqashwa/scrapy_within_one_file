import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime
import pandas as pd
# import json
# import numpy as np
# import urllib


class CilacapSpider(scrapy.Spider):
    name = 'cilacap'
    start_urls = [
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vRjGxvSiQjtQO7qSLj3umHBjodq0bTqOLnyYmvgXilPYoXj405WjVTOCumvl_yWg3bYWlV8oau0B_eK/pubhtml"
    ]

    custom_settings = {
        # 'ITEM_PIPELINES': {'DOWNLOAD_DELAY': 1},
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'cilacap.csv'
    }

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kecamatan'
        user_pic = 'Alfie Qashwa'
        date_update = datetime.now().strftime("%Y-%m-%d")
        provinsi = 'Jawa Tengah'
        kabkot = 'Cilacap'
        kecamatan = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[1]/text()')[4:-2].extract()
        kelurahan = ''
        alamat = ''
        total_odp = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[8]/text()')[2:-2].extract()
        total_pdp = ''
        total_positif = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[12]/text()')[1:-2].extract()
        positif_sembuh = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[11]/text()')[3:-2].extract()
        positif_dirawat = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[10]/text()')[2:-2].extract()
        positif_isolasi = ''
        positif_meninggal = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[9]/text()')[2:-2].extract()
        total_otg = ''
        odr_total = response.xpath(
            '//*[@id="1603347864"]/div/table/tbody/tr/td[4]/text()')[3:-2].extract()
        total_pp = ''
        total_ppdt = ''
        source_link = 'http://corona.cilacapkab.go.id/'

        for q in range(len(kecamatan)):
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan[q],
                'kelurahan': kelurahan,
                'alamat': alamat,
                'total_odp': total_odp[q],
                'total_pdp': total_pdp,
                'total_positif': total_positif[q],
                'positif_sembuh': positif_sembuh[q],
                'positif_dirawat': positif_dirawat[q],
                'positif_isolasi': positif_isolasi,
                'positif_meninggal': positif_meninggal[q],
                'total_otg': total_otg,
                'odr_total': odr_total[q],
                'total_pp': total_pp,
                'total_ppdt': total_ppdt,
                'source_link': source_link,
            }


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(CilacapSpider)
    process.start()
