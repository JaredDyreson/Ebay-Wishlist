#!/usr/bin/env python3.5

import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
import urllib.request
import os

class EbayItem():
	def __init__(self, url : str):
		self.url = url
		self.soup = BeautifulSoup(requests.get(self.url).text, 'lxml')
		self.item_name = self.get_name()
		self.image = self.get_image()
	def get_name(self):
		return self.soup.find(id="itemTitle").text.split("Details about")[1].strip()
	def get_image(self):
		return self.soup.find(id="mainImgHldr").find_all('img')[1]['src']
	def get_price(self):
		try: return self.soup.find(id="prcIsum_bidPrice")['content']
		except TypeError: return self.soup.find(id="prcIsum")['content']
	def get_currency(self):
		return self.soup.find(itemprop="priceCurrency")['content']
	def get_description(self):
		return self.soup.find(class_="itemAttr").text.strip()
	def convert_to_dict(self):
		return {
			"name": self.get_name(),
			"image_url": self.get_image(),
			"price": self.get_price(),
			"currency": self.get_currency()
		}
	def download_image(self):
		image_name = self.get_name().replace(" ", "_").lower()
		image_extentsion = os.path.basename(self.get_image()).split(".")[1]
		saved_image_location = "{}.{}".format(image_name, image_extentsion)
		if not(os.path.exists(saved_image_location)): urllib.request.urlretrieve(self.get_image(), saved_image_location)
		
example_item = EbayItem("https://www.ebay.com/itm/Genuine-OEM-Apple-Lightning-to-Headphone-Jack-AUX-Adapter-For-iPhone-7-8-X-3-5MM/173370134194?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20160908105057%26meid%3D676c5d6f8159432abae1e272202d0492%26pid%3D100675%26rk%3D2%26rkt%3D15%26mehot%3Dpp%26sd%3D193058503855%26itm%3D173370134194%26pmt%3D0%26noa%3D1%26pg%3D2481888&_trksid=p2481888.c100675.m4236&_trkparms=pageci%3Ad8d16259-c4bb-11e9-9344-74dbd180d50e%7Cparentrq%3Ab891f37516c0a4e8840d985dfff411e1%7Ciid%3A1")
example_item.download_image()
