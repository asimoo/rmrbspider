import scrapy
from rmrb.items import Website
from textrank4zh import TextRank4Keyword, TextRank4Sentence

class RmrbSpider(scrapy.Spider):
    name = "rmrb"
    allowed_domains = ["paper.people.com.cn"]
    start_urls = [
        "http://paper.people.com.cn/rmrb/html/2016-01/08/nw.D110000renmrb_20160108_1-01.htm"
        ]

    def parse(self,response):
        item = Website()
        itext = ''
        for sel0 in response.xpath("//div[@id='articleContent']"):
            itext = sel0.xpath('p/text()').extract()
        title1 = response.xpath('//h3/text()').extract()
        title2 = response.xpath('//h1/text()').extract()
        title3 = response.xpath('//h2/text()').extract()
        date = response.xpath("//div[@id='riqi_']/text()").extract()

        item['title1'] = title1[0].decode('gbk')
        item['title2'] = title2[0].decode('gbk')
        item['title3'] = title3[0].decode('gbk')
        item['date'] = date[0].decode('gbk')
        itext = ''.join(itext)
        itext = itext.decode('gbk')
        tr4w = TextRank4Keyword()

        tr4w.analyze(text=itext, lower=True, window=2)
        keylist = tr4w.get_keywords(10, word_min_len=2)
        item['keyword'] = keylist

        return item
        
