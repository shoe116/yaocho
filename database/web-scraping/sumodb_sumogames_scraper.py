#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
from selenium import webdriver
from bs4 import BeautifulSoup

class SumodbScraper(object):
    BASE_URL = "http://sumodb.sumogames.de/Results_text.aspx?b={0}&d={1}"
    LOG_PATH = "/tmp/SumodbScraper.log"
    PHANTOMJS_ARGS = [ '--proxy=proxy.server.no.basho:0000' ]
    TYPE_DRIVER = "driver"
    TYPE_REQUESTS = "requests"

    def __init__(self, log_path):
        #self.driver = webdriver.PhantomJS(service_args=self.PHANTOMJS_ARGS, service_log_path=log_path) 
        self.driver = webdriver.PhantomJS(service_log_path=log_path) 

    @classmethod
    def get_target_url(cls, year, basho, day):
        return cls.BASE_URL.format(year + basho, day)

    @classmethod
    def create_soup(cls, markup):
        return BeautifulSoup(markup, "html5lib")

    @classmethod
    def get_markup_by_requests(cls, url):
        res = requests.get(url)
        return res.text.encode(res.encoding)

    def get_markup_by_driver(self, url):
        print url
        self.driver.get(url)
        source = self.driver.page_source
        return source.encode("utf-8")

    def get_sorp(self, year, basho, day, type = TYPE_REQUESTS):
        url = self.get_target_url(year, basho, day)
        markup = ""
        if(type == self.TYPE_DRIVER):
            markup = self.get_markup_by_driver(url)
        else:
            markup = self.get_markup_by_requests(url)
        return self.create_soup(markup)

## test
if __name__ == '__main__':
    year = "2015"
    basho = "01"
    day = "9"
    
    scraper = SumodbScraper(SumodbScraper.LOG_PATH)
    print scraper.get_sorp(year, basho, day)
