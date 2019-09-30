from scrapy.item import Item

class TestItem(Item):
    name = Field()
    position = Field()
    cap = Field()