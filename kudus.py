import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime
# import json
# import numpy as np
# import urlli


class KudusSpider(scrapy.Spider):
    name = "kudus"
    start_urls = [
        "https://corona.kuduskab.go.id/"
    ]

    custom_settings = {
        # 'ITEM_PIPELINES': {'DOWNLOAD_DELAY': 1},
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'kudus.csv'
    }

    # convert months string into number
    months = dict(Januari='01', Februari='02', Maret='03', April='04', Mei='05', Juni='06',
                  Juli='07', Agustus='08', September='09', Oktober='10', November='11', Desember='12')

    def parse(self, response):
        scrape_date = datetime.now().strftime("%Y-%m-%d")
        types = "kecamatan"
        user_pic = "Alfie Qashwa"
        crawl_date = response.xpath(
            '//*[@id="monitoring"]/div/div/div/div/div[1]/span/text()').re(r': (\w+) (\w+) (\w+)')
        # s**t dirty code
        # updated: using regex
        day = crawl_date[0]
        month = crawl_date[1]
        year = crawl_date[2]
        date_update = year + '-' + self.months[month] + '-' + day
        provinsi = 'Jawa Tengah'
        kabkot = 'Kudus'
        kecamatan = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[1]/text()').extract()
        kelurahan = ''
        alamat = ''
        total_odp = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[3]/text()').extract()
        total_pdp = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[4]/text()').extract()
        total_positif = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[5]/text()').extract()
        positif_dirawat = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[6]/text()').extract()
        positif_isolasi = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[7]/text()').extract()
        positif_sembuh = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[8]/text()').extract()
        positif_meninggal = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[9]/text()').extract()
        total_otg = ''
        odr_total = response.xpath(
            '//*[@id="about"]/div/div/div/div/div/div/span/div/div/table/tbody/tr/td[2]/text()').extract()
        total_pp = ''
        total_ppdt = ''
        source_link = 'https://corona.kuduskab.go.id/'

        for q in range(len(kecamatan)):
            yield {
                'scrape_date': scrape_date,
                'types': types,
                'user_pic': user_pic,
                'date_update': date_update,
                'provinsi': provinsi,
                'kabkot': kabkot,
                'kecamatan': kecamatan[q].capitalize(),
                'kelurahan': kelurahan,
                'alamat': alamat,
                'total_odp': total_odp[q],
                'total_pdp': total_pdp[q],
                'total_positif': total_positif[q],
                'positif_sembuh': positif_sembuh[q],
                'positif_dirawat': positif_dirawat[q],
                'positif_isolasi': positif_isolasi[q],
                'positif_meninggal': positif_meninggal[q],
                'total_otg': total_otg,
                'odr_total': odr_total[q],
                'total_pp': total_pp,
                'total_ppdt': total_ppdt,
                'source_link': source_link,
            }


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(KudusSpider)
    process.start()
