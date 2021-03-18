import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime
import pandas as pd
import json
# import numpy as np
# import urllib


class PurbalinggaSpider(scrapy.Spider):
    name = 'purbalingga'
    start_urls = [
        "https://petatematik.purbalinggakab.go.id/api/corona/data/geoJSON"
    ]
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://petatematik.purbalinggakab.go.id/peta/monitoring-corona",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    custom_settings = {
        # 'ITEM_PIPELINES': {'DOWNLOAD_DELAY': 1},
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'purbalingga.csv'
    }

    def parse(self, response):
        raw_data = response.body
        datas = json.loads(raw_data)
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = 'kecamatan'
        user_pic = 'Alfie Qashwa'
        date_update = datetime.now().strftime("%Y-%m-%d")
        provinsi = 'Jawa Tengah'
        kabkot = 'Purbalingga'
        source_link = 'https://corona.purbalinggakab.go.id/'

        for data in datas:
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': data["properties"]["name"],
                'kelurahan': '',
                'alamat': '',
                'total_odp': data["properties"]["odp_total"],
                'total_pdp': data["properties"]["pdp_total"],
                'total_positif': data["properties"]["positif_total"],
                'positif_sembuh': data["properties"]["positif_sembuh"],
                'positif_dirawat': data["properties"]["positif_dirawat"],
                'positif_isolasi': '',
                'positif_meninggal': data["properties"]["positif_meninggal"],
                'total_otg': '',
                'odr_total': '',
                'total_pp': '',
                'total_ppdt': '',
                'source_link': source_link,
            }


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(PurbalinggaSpider)
    process.start()
