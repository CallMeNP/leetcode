# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QuestionItem(scrapy.Item):
    id = scrapy.Field()
    frontend_id = scrapy.Field()
    title_zh = scrapy.Field()
    title_en = scrapy.Field()
    slug_title = scrapy.Field()
    difficulty = scrapy.Field()
    paid_only = scrapy.Field()


class RelationItem(scrapy.Item):
    question_frontend_id = scrapy.Field()
    question_id = scrapy.Field()
    tag_id = scrapy.Field()
    tag_slug = scrapy.Field()
