#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""

import scrapy
import json
from os.path import dirname, realpath
from ..items import RelationItem


class RelationSpider(scrapy.Spider):
    name = 'relation'

    def start_requests(self):
        path = dirname(realpath(__file__)) + "/topics.json"
        topics = json.load(open(path))
        url = 'https://leetcode-cn.com/graphql'
        for t in topics:
            graphql_veriables = '"variables":{"slug":"%s"},' % t['slug']
            graphql = r'{"operationName":"getTopicTag",' + graphql_veriables + \
                      r'"query":"query getTopicTag($slug: String!) {\n' \
                      r'  topicTag(slug: $slug) {\n' \
                      r'    name\n' \
                      r'    translatedName\n' \
                      r'    questions {\n' \
                      r'      status\n' \
                      r'      questionId\n' \
                      r'      questionFrontendId\n' \
                      r'      title\n' \
                      r'      titleSlug\n' \
                      r'      translatedTitle\n' \
                      r'      stats\n' \
                      r'      difficulty\n' \
                      r'      isPaidOnly\n' \
                      r'      topicTags {\n' \
                      r'        name\n' \
                      r'        translatedName\n' \
                      r'        slug\n' \
                      r'        __typename\n' \
                      r'      }\n' \
                      r'      companyTags {\n' \
                      r'        name\n' \
                      r'        translatedName\n' \
                      r'        slug\n' \
                      r'        __typename\n' \
                      r'      }\n' \
                      r'      __typename\n' \
                      r'    }\n' \
                      r'    frequencies\n' \
                      r'    __typename\n' \
                      r'  }\n' \
                      r'  favoritesLists\n' \
                      r'}\n' \
                      r'"}'
            print(graphql_veriables)
            yield scrapy.Request(url=url, meta={'topic': t.copy()}, body=graphql, callback=self.parse)

    def parse(self, response):
        """
        :param self:
        :type response: scrapy.Response
        :return:
        """
        data = json.loads(response.text)
        for r in data['data']['topicTag']['questions']:
            relation = RelationItem()
            relation['tag_id'] = response.meta['topic']['id']
            relation['tag_slug'] = response.meta['topic']['slug']
            relation['question_id'] = r['questionId']
            relation['question_frontend_id'] = r['questionFrontendId']
            yield relation
