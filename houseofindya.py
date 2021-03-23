import scrapy
from ..items import HouseofindyaItem


class Information(scrapy.Spider):
    name = 'info'
    start_urls = {
        'https://www.houseofindya.com/zyra/necklace-sets/cat'
    }

    def parse(self, response):
        items = HouseofindyaItem()

        all_list = response.css('#JsonProductList li')

        for q in all_list:
            title = q.css('p::text').extract()
            discount = q.css('.catgItem span::text').extract()
            color = q.css('li::attr(data-color)').extract()
            total_price = q.css('span+ span::text').extract()
            discount_price = q.css('span:nth-child(1)::text').extract()
            image_link = q.css('.lazy::attr(data-original)').extract()

            items['a_title'] = title
            items['d_discount'] = discount
            items['b_color'] = color
            items['c_total_price'] = total_price
            items['e_discount_price'] = discount_price
            items['f_image_link'] = image_link

            yield items
