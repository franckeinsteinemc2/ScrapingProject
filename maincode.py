import scrapy
from scrapy import Selector
import requests

url="https://www.lancome.fr/"

html=requests.get(url).content

sel=Selector(text=html)

print(sel.css('*').extract())
