import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime
import pandas as pd
# import json
# import numpy as np
# import urllib


class BanjarnegaraSpider(scrapy.Spider):
    name = "banjarnegara"
    start_urls = [
        # "http://corona.banjarnegarakab.go.id/"
        "https://corona.jatengprov.go.id/data"
    ]

    custom_settings = {
        # 'ITEM_PIPELINES': {'DOWNLOAD_DELAY': 1},
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'banjarnegara.csv'
    }

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kabupaten'
        user_pic = 'Alfie Qashwa'
        date_update = scrape_date
        provinsi = 'Jawa Tengah'
        kabkot = 'Banjarnegara'
        kecamatan = ''
        kelurahan = ''
        alamat = ''
        total_odp = response.xpath(
            '//*[@id="pills-domisili3"]/div[1]/table/tbody/tr[30]/td[6]/text()').get()
        total_pdp = ''
        total_positif = response.xpath(
            '//*[@id="pills-domisili3"]/div[1]/table/tbody/tr[30]/td[2]/text()').get()
        positif_sembuh = response.xpath(
            '//*[@id="pills-domisili3"]/div[1]/table/tbody/tr[30]/td[4]/text()').get()
        positif_dirawat = response.xpath(
            '//*[@id="pills-domisili3"]/div[1]/table/tbody/tr[30]/td[3]/text()').get()
        positif_isolasi = ''
        positif_meninggal = response.xpath(
            '//*[@id="pills-domisili3"]/div[1]/table/tbody/tr[30]/td[5]/text()').get()
        total_otg = ''
        odr_total = ''
        total_pp = ''
        total_ppdt = ''
        source_link = "http://corona.banjarnegarakab.go.id/"

        yield {
            'scrape_date': scrape_date,
            'types': types,
            'user_pic': user_pic,
            'date_update': date_update,
            'provinsi': provinsi,
            'kabkot': kabkot,
            'kecamatan': kecamatan,
            'kelurahan': kelurahan,
            'alamat': alamat,
            'total_odp': total_odp.replace('.', ''),
            'total_pdp': total_pdp,
            'total_positif': total_positif.replace('.', ''),
            'positif_sembuh': positif_sembuh.replace('.', ''),
            'positif_dirawat': positif_dirawat.replace('.', ''),
            'positif_isolasi': positif_isolasi,
            'positif_meninggal': positif_meninggal.replace('.', ''),
            'total_otg': total_otg,
            'odr_total': odr_total,
            'total_pp': total_pp,
            'total_ppdt': total_ppdt,
            'source_link': source_link,
        }


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(BanjarnegaraSpider)
    process.start()
