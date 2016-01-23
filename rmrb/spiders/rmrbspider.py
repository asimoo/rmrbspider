import scrapy, datetime
from rmrb.items import Website
from textrank4zh import TextRank4Keyword, TextRank4Sentence

def CreateUrl(begin, end):
        urlpart1 = "http://paper.people.com.cn/rmrb/html/"
        urlpart2 = "/nw.D110000renmrb_"
        postfix = ".htm"
        urllist = []
        for i in range((end - begin).days+1):
            today = begin + datetime.timedelta(days=i)
            year = today.strftime('%Y')
            month = today.strftime('%m')
            day = today.strftime('%d')
            todaystr = today.strftime('%Y%m%d')
            for j in range(1,6):
                    for k in range(1,4):
                            tempurl = urlpart1 + year + "-" + month + "/" + day + urlpart2 + todaystr + "_" + str(j) +"-0" + str(k) +postfix
                            urllist.append(tempurl)
        return urllist

class RmrbSpider(scrapy.Spider):
    name = "rmrb"
    allowed_domains = ["paper.people.com.cn"]
    begin = datetime.date(2016,1,5)
    end = datetime.date(2016,1,11)
    start_urls = CreateUrl(begin, end)
    
##    start_urls = [
##        "http://paper.people.com.cn/rmrb/html/2016-01/08/nw.D110000renmrb_20160108_1-01.htm",
##        "http://paper.people.com.cn/rmrb/html/2016-01/11/nw.D110000renmrb_20160111_1-01.htm"
##        ]
##    print start_urls

    def parse(self,response):
        item = Website()
        itext = ''
        for sel0 in response.xpath("//div[@id='articleContent']"):
            itext = sel0.xpath('p/text()').extract()
        title1 = response.xpath('//h3').extract()
        title2 = response.xpath('//h1').extract()
        title3 = response.xpath('//h2').extract()
        date = response.xpath("//div[@id='riqi_']/text()").extract()

        item['title1'] = title1[0].decode('utf-8')+"\n"
        item['title2'] = title2[0].decode('utf-8')+"\n"
        item['title3'] = title3[0].decode('utf-8')+"\n"
        item['date'] = date[0].decode('utf-8')+"\n"
        itext = '\n'.join(itext)
        itext = itext.decode('utf-8')
        item['text'] = itext+"\n"
        tr4w = TextRank4Keyword()

        tr4w.analyze(text=itext, lower=True, window=3)
        keylist = tr4w.get_keywords(10, word_min_len=2)
        wordlist = []
        for listitem in keylist:
            word = listitem.word
            wordlist.append(word.decode('utf-8'))
        wordlist.append("\n")
        item['keyword'] = wordlist

        return item


    
            
        
