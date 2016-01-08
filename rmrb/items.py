from scrapy.item import Item,Field

class Website(Item):

    title1 = Field()
    title2 = Field()
    title3 = Field()
    date = Field()
    text = Field()
    keyword = Field()
