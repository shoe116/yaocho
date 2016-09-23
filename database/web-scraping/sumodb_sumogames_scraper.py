#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib

class SumodbScraper(object):
    BASE_URL = "http://sumodb.sumogames.de/Results_text.aspx?b={0}&d={1}"
    LOG_PATH = "/tmp/SumodbScraper.log"

    def __init__(self, log_path):
        self.scraping = ScrapingLib(log_path)

    @classmethod
    def get_target_url(cls, year, basho, day):
        return cls.BASE_URL.format(year + basho, day)

    def get_sorp(self, year, basho, day, type):
        url = self.get_target_url(year, basho, day)
        return self.scraping.get_sorp(url, type)

## test
if __name__ == '__main__':
    year = "2015"
    basho = "01"
    day = "9"
    
    scraper = SumodbScraper(SumodbScraper.LOG_PATH)
    print scraper.get_sorp(year, basho, day, "")
