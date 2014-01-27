from scrapy.spider import Spider
from scrapy.selector import Selector
from zhihu_stats.items import ZhihuUser
import simplejson as json

class ZhihuSpider(Spider):
    #http_user = "tangerinewhite32@gmail.com"
    #http_pass = "Cd\5932e35"
    name = "zhihu"
    allowed_domains = ["zhihu.com"]

    def __init__(self, username=None, *args, **kwargs):
        super(ZhihuSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["http://www.zhihu.com/people/%s" % username]

    def parse(self, response):
        selector = Selector(response)
        user = ZhihuUser()
        user['name'] = selector.xpath("//span[@class='name']/text()").extract()[0]
        user['location'] = selector.xpath('//span[@class="location item"]/@title').extract()[0]
        networking = selector.xpath('//a[@class="item"]/strong/text()').extract()
        user['followees'] = networking[0]
        user['followers'] = networking[1] 
        user['upvotes'] = selector.xpath('//span[@class="zm-profile-header-user-agree"]/strong/text()').extract()[0]
        user['thanks'] = selector.xpath('//span[@class="zm-profile-header-user-thanks"]/strong/text()').extract()[0]
        statistics = selector.xpath('//div[@class="profile-navbar clearfix"]/a/span/text()').extract()
        user['questions'] = statistics[1]
        user['answers'] = statistics[2]
        user['essays'] = statistics[3]
        user['bookmarks'] = statistics[4]
        user['edits'] = statistics[5]
        print ""
        print user['name']
        print user['location']
        print user['followees']
        print user['followers']
        print user['upvotes']
        print user['thanks']
        print user['questions']
        print user['answers']
        print user['essays']
        print user['bookmarks']
        print user['edits']
        print ""
