# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ComputerdepartmentSpider(CrawlSpider):
	name = "computerDepartment"
	allowed_domains = ["www.imdb.com/"]
	start_urls = ['http://www.imdb.com/search/title?groups=top_250&sort=user_rating']
	"""
	rules = (
		Rule(LinkExtractor(allow=(), restrict_css=('.meta-item-comments',)),
			 callback="parse_item",
			 follow=True),)
	"""

	def parse(self, response):
		#Extracting the content using css selectors
		movieName = response.css('.lister-item-header::attr(a)').extract()
		links = response.xpath('//a[contains(@href, "image")]/img/@src').extract()
		"""
		titles = response.css('.title.may-blank::text').extract()
		votes = response.css('.score.unvoted::text').extract()
		times = response.css('time::attr(title)').extract()
		comments = response.css('.comments::text').extract()
	    """

		#Give the extracted content row wise
		for item in zip(movieName):
			#create a dictionary to store the scraped info
			scraped_info = {
				'movie' : item
			}

			#yield or give the scraped info to scrapy
			yield scraped_info

"""
	def parse_item(self, response):
		print("Processing ",response.url)
"""