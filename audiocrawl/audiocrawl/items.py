# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AudiocrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    audio_info_title = scrapy.Field()
    audio_info_preimg = scrapy.Field()
    audio_info_url = scrapy.Field()
    audio_info_author = scrapy.Field()
    audio_info_play_author = scrapy.Field()
    audio_info_describe = scrapy.Field()


class DownloadautioItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    file_name = scrapy.Field()
    link_url = scrapy.Field()
    down_url = scrapy.Field()
    file_path = scrapy.Field()
    audio_title = scrapy.Field()
