# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseofindyaItem(scrapy.Item):
    # define the fields for your item here like:
    a_title = scrapy.Field()
    d_discount = scrapy.Field()
    b_color = scrapy.Field()
    c_total_price = scrapy.Field()
    e_discount_price = scrapy.Field()
    f_image_link = scrapy.Field()

