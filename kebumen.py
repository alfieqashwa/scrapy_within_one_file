import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime
import pandas as pd
# import json
import numpy as np
# import urllib


class KebumenSpider(scrapy.Spider):
    name = "kebumen"

    custom_settings = {
        # 'ITEM_PIPELINES': {'DOWNLOAD_DELAY': 1},
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'kebumen.csv'
    }

    def start_requests(self):
        site = "https://corona.kebumenkab.go.id/index.php/web/data_sebaran_by_desa/"
        urls = [
            f'{site}01',
            f'{site}02',
            f'{site}03',
            f'{site}04',
            f'{site}05',
            f'{site}06',
            f'{site}07',
            f'{site}08',
            f'{site}09',
            f'{site}10',
            f'{site}11',
            f'{site}12',
            f'{site}13',
            f'{site}14',
            f'{site}15',
            f'{site}16',
            f'{site}17',
            f'{site}18',
            f'{site}19',
            f'{site}20',
            f'{site}21',
            f'{site}22',
            f'{site}23',
            f'{site}24',
            f'{site}25',
            f'{site}26',
            # Remote Address: 103.86.103.62:443
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        scrape_date = datetime.now().strftime('%Y-%m-%d')
        types = 'kelurahan'
        user_pic = 'Alfie Qashwa'
        date_update = datetime.now().strftime('%Y-%m-%d')
        provinsi = 'Jawa Tengah'
        kabkot = 'Kebumen'
        kecamatan = response.xpath(
            '/html/body/div/div[1]/h3/span/text()').get().split(' ')
        kelurahan = response.xpath(
            '/html/body/div/div/div/table/tbody/tr/td[2]/text()').getall()
        alamat = ''
        odp_dirawat = np.array(list(map(int, response.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr/td[3]/text()').getall())))
        odp_dirujuk = np.array(list(map(int, response.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr/td[4]/text()').getall())))
        odp_isolasi = np.array(list(map(int, response.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr/td[5]/text()').getall())))
        list_total_odp_np = odp_dirawat+odp_dirujuk+odp_isolasi
        list_total_odp = list_total_odp_np.tolist()

        pdp_dirawat = np.array(list(map(int, response.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr/td[6]/text()').getall())))
        pdp_dirujuk = np.array(list(map(int, response.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr/td[7]/text()').getall())))
        pdp_isolasi = np.array(list(map(int, response.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr/td[8]/text()').getall())))
        pdp_meninggal = np.array(list(map(int, response.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr/td[9]/text()').getall())))
        list_total_pdp_np = pdp_dirawat+pdp_dirujuk+pdp_isolasi+pdp_meninggal
        list_total_pdp = list_total_pdp_np.tolist()

        positif_sembuh_np = np.array(list(map(int, response.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr/td[14]/text()').getall())))
        list_positif_sembuh = positif_sembuh_np.tolist()
        positif_dirawat_np = np.array(list(map(int, response.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr/td[10]/text()').getall())))
        list_positif_dirawat = positif_dirawat_np.tolist()
        positif_isolasi_np = np.array(list(map(int, response.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr/td[12]/text()').getall())))
        list_positif_isolasi = positif_isolasi_np.tolist()
        positif_meninggal_np = np.array(list(map(int, response.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr/td[13]/text()').getall())))
        list_positif_meninggal = positif_meninggal_np.tolist()

        list_total_positif_np = positif_sembuh_np+positif_dirawat_np + \
            positif_isolasi_np+positif_meninggal_np
        list_total_positif = list_total_positif_np.tolist()

        source_link = 'https://corona.kebumenkab.go.id/'

        for q in range(len(kelurahan)):
            total_odp = list_total_odp[q]
            total_pdp = list_total_pdp[q]
            total_positif = list_total_positif[q]
            positif_sembuh = list_positif_sembuh[q]
            positif_dirawat = list_positif_dirawat[q]
            positif_isolasi = list_positif_isolasi[q]
            positif_meninggal = list_positif_meninggal[q]
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan[1].capitalize(),
                'kelurahan': kelurahan[q],
                'alamat': alamat,
                'total_odp': total_odp,
                'total_pdp': total_pdp,
                'total_positif': total_positif,
                'positif_sembuh': positif_sembuh,
                'positif_dirawat': positif_dirawat,
                'positif_isolasi': positif_isolasi,
                'positif_meninggal': positif_meninggal,
                'total_otg': '',
                'odr_total': '',
                'total_pp': '',
                'total_ppdt': '',
                'source_link': source_link,
            }


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(KebumenSpider)
    process.start()


