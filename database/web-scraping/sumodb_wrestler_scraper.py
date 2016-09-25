#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib

class SumodbWrestlerScraper(object):
    BASE_URL = "http://sumodb.sumogames.de/Rikishi_text.aspx?r={0}"
    LOG_PATH = "/tmp/sumodb_wrestler_scraper.log"

    def __init__(self, log_path):
        self.scraping = ScrapingLib(log_path)

    @classmethod
    def get_target_url(cls, rikishiId):
        return cls.BASE_URL.format(rikishiId)

    def get_sorp(self, rikishiId, type):
        url = self.get_target_url(rikishiId)
        return self.scraping.get_sorp(url, type)

## test
if __name__ == '__main__':
    rikishiId = "9"
    
    scraper = SumodbWrestlerScraper(SumodbWrestlerScraper.LOG_PATH)
    print scraper.get_sorp(rikishiId, "")
