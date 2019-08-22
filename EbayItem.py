#!/usr/bin/env python3.5

import requests
from bs4 import BeautifulSoup

class EbayItem():
	def __init__(self, url : str):
		self.url = url
		self.soup = BeautifulSoup(requests.get(self.url).text, 'lxml')
		self.item_name = self.get_name()
		self.image = self.get_image()
	def get_name(self):
		return self.soup.find(id="itemTitle").text.split("Details about")[1].strip()
	def get_image(self):
		return self.soup.find(id="icImg").text
	def get_price(self):
		return self.soup.find(id="prcIsum_bidPrice")['content']
	def get_currency(self):
		return self.soup.find(itemprop="priceCurrency")['content']
	def get_description(self):
		return self.soup.find(class_="itemAttr").text.strip()
example_item = EbayItem("https://www.ebay.com/itm/1998-Honda-Civic/193058503855?hash=item2cf32efcaf:g:vzoAAOSwFTBdXH~F#viTabs_0")

print("Name: {}".format(example_item.item_name))
print("Price: {}".format(example_item.get_price()))
print("Currency: {}".format(example_item.get_currency()))
