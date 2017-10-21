# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import BaseSpider
import re

class ComputerdepartmentSpider(CrawlSpider):
	name = "computerDepartment"
	allowed_domains = ["uiowa.edu"]
	start_urls = ['https://uiowa.edu/']
#	allowed_domains = ['packtpub.com']
#	start_urls = ["https://www.packtpub.com"]
	"""
	rules = (
		Rule(LinkExtractor(allow=(), restrict_css=('.meta-item-comments',)),
			 callback="parse_item",
			 follow=True),)
	"""

	def parse(self, response):
		#Extracting the content using css selectors
		#movieName = response.css('.lister-item-header::text').extract()
		hxs = Selector(response)
		visited_links=[]
		url = ""
		links = response.xpath('//a/@href').extract()
		link_validator= re.compile("^(?:http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")
		print("LINSK FOUND IN THE FILE ARE ",links)

		for i in range(len(links)):
			#print("links -> ",links[i])
			links[i] = "https://uiowa.edu"+links[i]
			if link_validator.match(links[i]) and not links[i] in visited_links:
				scraped_info = {
					'links' : links[i]
				}
				visited_links.append(links[i])
				yield scraped_info
				url = str(links[i])
				print(" URL IS -> ",url)
				yield Request(url, self.parse)


"""
		for link in links:
			yield Request(link, self.parse)

		for link in links:
			if link_validator.match(link) and not link in visited_links:
				visited_links.append(link)
				yield Request(link, self.parse)
			else:
				full_url=response.urljoin(link)
				visited_links.append(full_url)
				yield Request(full_url, self.parse)
				

		le = LinkExtractor() # empty for getting everything, check different options on documentation
		for link in le.extract_links(response):
			yield Request(link.url, callback=self.parse)

		links = response.xpath('//div[@class = "lister-item-content"]/h3/a/text()').extract()
		titles = response.css('.title.may-blank::text').extract()
		votes = response.css('.score.unvoted::text').extract()
		times = response.css('time::attr(title)').extract()
		comments = response.css('.comments::text').extract()

		#Give the extracted content row wise
		for item in zip(links):
			#create a dictionary to store the scraped info
			scraped_info = {
				'links' : item
			}

			#yield or give the scraped info to scrapy
			yield scraped_info
"""

"""
	def parse_item(self, response):
		print("Processing ",response.url)
"""	