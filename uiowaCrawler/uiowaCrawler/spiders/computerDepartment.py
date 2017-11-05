# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import BaseSpider
import re

global_links=set()

class ComputerdepartmentSpider(CrawlSpider):
	name = "computerDepartment"
	allowed_domains = ["uiowa.edu"]
	start_urls = ['https://uiowa.edu/']

	def parse(self, response):
		#Extracting the content using css selectors
		#movieName = response.css('.lister-item-header::text').extract()
		hxs = Selector(response)
		visited_links=[]
		url = ""
		links = response.xpath('//a/@href').extract()
		link_validator= re.compile("^(?:http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")
		#print("LINKS FOUND IN THE FILE ARE ",links)



		for i in range(len(links)):
			#print("links -> ",links[i])
			global global_links
			if not links[i].startswith("http") and "mailto" not in links[i]: #to remove email to me links in web pages
				links[i] = "https://uiowa.edu"+links[i]
			if link_validator.match(links[i]) and not links[i] in visited_links:
				scraped_info = {
					'links' : links[i],
					'URL' : response.url
				}
				visited_links.append(links[i])
				if not response.url in global_links:
					global_links.add(response.url)

				yield scraped_info
				url = str(links[i])
				#print(" URL IS -> ",url)
				if not url in global_links:
					yield Request(url, self.parse)
		#print("The global links are ",global_links)
		#have to ignore lib.uiowa as it has database of books 
# nohup scrapy crawl computerDepartment &

