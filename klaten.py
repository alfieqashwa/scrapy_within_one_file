import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime
import pandas as pd
import json
# import numpy as np
# import urllib


class KlatenSpider(scrapy.Spider):
    name = 'klaten'
    start_urls = [
        "https://awasicorona.klatenkab.go.id/piechart"
    ]
    headers = {
        "Accept": "Accept: application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://awasicorona.klatenkab.go.id/piechart",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    custom_settings = {
        # 'ITEM_PIPELINES': {'DOWNLOAD_DELAY': 1},
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'klaten.csv'
    }

    def parse(self, response):
        raw_data = response.body
        data = json.loads(raw_data)

        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kabupaten'
        user_pic = 'Alfie Qashwa'
        # they will fetch the datas everyday automatically as data-fetching habits
        date_update = datetime.now().strftime("%Y-%m-%d")
        provinsi = 'Jawa Tengah'
        kabkot = 'Klaten'
        kecamatan = ''
        kelurahan = ''
        alamat = ''
        total_odp = data[2][1] + data[3][1]
        total_pdp = ''
        positif_sembuh = data[10][1]
        positif_dirawat = data[0][1]
        positif_isolasi = data[9][1]
        positif_meninggal = data[11][1]
        total_otg = ''
        odr_total = ''
        total_pp = ''
        total_ppdt = ''
        source_link = 'https://awasicorona.klatenkab.go.id/'

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
            'total_odp': total_odp,
            'total_pdp': total_pdp,
            'total_positif': positif_sembuh+positif_dirawat+positif_isolasi+positif_meninggal,
            'positif_sembuh': positif_sembuh,
            'positif_dirawat': positif_dirawat,
            'positif_isolasi': positif_isolasi,
            'positif_meninggal': positif_meninggal,
            'total_otg': total_otg,
            'odr_total': odr_total,
            'total_pp': total_pp,
            'total_ppdt': total_ppdt,
            'source_link': source_link,
        }


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(KlatenSpider)
    process.start()
