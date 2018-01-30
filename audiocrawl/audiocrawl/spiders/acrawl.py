# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

from audiocrawl.items import AudiocrawlItem

from audiocrawl.spiders import crawl_audio_db
from audiocrawl.items import DownloadautioItem

from audiocrawl.spiders.t_models import AudioListDb


class AcrawlSpider(scrapy.Spider):
    name = 'acrawl'
    allowed_domains = ['www.520tingshu.com']

    def __init__(self):
        self.server_url = 'http://www.520tingshu.com'
        self.start_urls = ['http://www.520tingshu.com']
        crawl_audio_db.init()

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.cparseIndex)

    def cparseIndex(self, response):
        sel = Selector(response)
        classifys = sel.xpath(
            '//div[re:test(@id,"navbar|sform")]//ul/li//a[re:test(@href, "^/list/list.{1,5}.html")]')  # 爬取首页分类链接
        # classifys = []
        for i in range(len(classifys)):
            classifyNode = classifys[i]

            href = classifyNode.xpath('@href').extract_first()
            title = classifyNode.xpath(
                '//div[re:test(@id,"navbar|sform")]//ul/li//a[re:test(@href, "^/list/list.{1,5}.html")]//text()')[
                i].extract()
            # print("href:" + str(href + ",title:" + str(title)))
            if crawl_audio_db.have_classify_count(title) == 0:
                crawl_audio_db.addClassify(audio_classify_name=title)
            else:
                print(title + "，已经存在")
            yield scrapy.Request(url=self.server_url + href, meta={'classify': title}, callback=self.parseClassifyList)

    def parseClassifyList(self, response):
        sel = Selector(response)
        classify = response.meta['classify']
        totalCount = sel.xpath(
            '//div[re:test(@id,"baybox")]/div[1]/div[re:test(@class,"page")]/span/span[1]/text()').extract_first()
        print("totalCount:" + totalCount + ",url:" + response.url)

        count = totalCount.split(':')[1].split('/')[1].replace("页", "")
        print("count:" + count)
        linkurls = [count]
        audio_url = response.url
        linkurls.append(audio_url)
        audio_url = audio_url[:-5]

        for link in range(2, int(count) + 1):
            total_url = audio_url + "_" + str(link) + ".html"
            # print("total:" + total_url)
            linkurls.append(total_url)
        # print("linkurls:" + str(linkurls))

        for i in range(1, len(linkurls)):
            linkurl = str(linkurls[i])
            # print("linkurl:" + linkurl)
            yield scrapy.Request(url=str(linkurl), meta={'classify': classify}, callback=self.parseList)

    def parseList(self, response):
        sel = Selector(response)
        audioList = sel.xpath('//div[re:test(@id,"baybox")]/div[1]//ul/li')
        items = []
        classify_t = response.meta['classify']
        print("classify:" + classify_t)
        for index in range(len(audioList)):
            item = AudiocrawlItem()
            audio_info_sel = audioList[index]
            img = audio_info_sel.xpath('dl/dt/a/img/@src').extract_first()
            title = audio_info_sel.xpath('dl/dd[1]/h2/a/@title').extract_first()
            url = audio_info_sel.xpath('dl/dd[1]/h2/a/@href').extract_first()
            audio_author = audio_info_sel.xpath('dl/dd[2]/span/text()').extract_first()
            audio_describe = audio_info_sel.xpath('dl/dd[6]/text()').extract_first()
            play_author = audio_info_sel.xpath('dl/dd[3]/text()').extract_first()
            item['audio_info_title'] = title
            item['audio_info_preimg'] = img
            item['audio_info_url'] = url
            item['audio_info_author'] = audio_author
            item['audio_info_play_author'] = play_author
            item['audio_info_describe'] = audio_describe
            classify = crawl_audio_db.getClassifyIdByName(classify_t)

            ald = AudioListDb(audio_info_title=title, audio_info_preimg=img, audio_info_url=url,
                              audio_info_author=audio_author, audio_info_play_author=play_author,
                              audio_info_describe=audio_describe, audio_classify_db_id=classify.id)
            if crawl_audio_db.have_audio_count(title) == 0:
                crawl_audio_db.addAudioListDb(ald)
            else:
                print(title + ",已经存在")
            items.append(item)

        for item in items:
            url = item['audio_info_url']
            print("url:" + url)
            yield scrapy.Request(url=self.server_url + url, meta={'item:': item}, callback=self.parse1)

    def parse1(self, response):
        sel = Selector(response)
        aTagList = sel.xpath('//li//a[re:test(@href, "/down/?.{3,20}$")]')
        audio_title = sel.xpath('//*[@id="baybox"]/div/div[1]/dl/dd[1]//h2/text()').extract_first()
        items = []
        for index in range(len(aTagList)):
            item = DownloadautioItem()
            cl = aTagList[index]
            title = cl.xpath('@title').extract_first()
            url = str(cl.xpath("@href").extract_first())
            strQuestionMarkIndex = url.index('?')
            strPeriodIndex = url.index('.')
            newUrl = url[strQuestionMarkIndex + 1:strPeriodIndex]
            list = newUrl.split('-')
            id = list[0]
            pid = list[1]
            vid = list[2]
            newUrl = '/xunleidown/?id=' + id + '&vid=' + vid + '&pid=' + pid

            tUrl = self.server_url + newUrl
            item['link_url'] = str(tUrl)
            item['file_name'] = title
            item['audio_title'] = audio_title

            items.append(item)
        for item in items:
            url = item['link_url']
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        item['link_url'] = response.url
        sel = Selector(response)
        downloadUrl = sel.xpath('//a/@thunderhref').extract_first()
        item['down_url'] = downloadUrl
        print("audio_title:" + item['audio_title'])
        aldi = crawl_audio_db.getAudioIdByTitle(item['audio_title'])
        audio_title = item['audio_title']
        audio_detail_title = item['file_name']
        if crawl_audio_db.have_audio_deitail_item_count(audio_title, audio_detail_title) == 0:
            crawl_audio_db.addAudioDetail(audio_title=audio_title, audio_detail_title=audio_detail_title,
                                          audio_detail_url=item['down_url'], audio_list_db_id=aldi.id)
        else:
            print(audio_title + "," + audio_detail_title + ",已经存在")
        yield item
