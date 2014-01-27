# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ZhihuUser(Item):
    name = Field()
    location = Field()
    followees = Field()
    followers = Field()
    upvotes = Field()
    thanks = Field()
    questions = Field()
    answers = Field()
    essays = Field()
    bookmarks = Field()
    edits = Field()
