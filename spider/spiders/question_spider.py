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
from ..items import QuestionItem


class QuestionSpider(scrapy.Spider):
    name = "question"

    def start_requests(self):
        # graphql 中的 \n 不能被当做转义处理，所以要用前缀r，声明此字符串是raw的。
        graphql = r'{"operationName":"getQuestionTranslation",' \
                  r'"variables":{},' \
                  r'"query":"query getQuestionTranslation($lang: String) {\n' \
                  r'  translations: allAppliedQuestionTranslations(lang: $lang) {\n' \
                  r'    title\n' \
                  r'    question {\n' \
                  r'      questionId\n' \
                  r'      __typename\n' \
                  r'    }\n' \
                  r'    __typename\n' \
                  r'  }\n' \
                  r'}\n' \
                  r'"}'
        url = "https://leetcode-cn.com/graphql"
        yield scrapy.Request(url=url, body=graphql, callback=self.parse_title_zh)

    def parse(self, response):
        """
        解析所有题目
        :type response: scrapy.http.response.Response
        :rtype: int
        """
        data = json.loads(response.text)
        for q in data['stat_status_pairs']:
            question = QuestionItem()
            question['id'] = q['stat']['question_id']
            question['frontend_id'] = q['stat']['frontend_question_id']
            question['title_en'] = q['stat']['question__title']
            question['title_zh'] = response.meta['translations'].get(int(question['id']), '')
            question['slug_title'] = q['stat']['question__title_slug']
            question['difficulty'] = q['difficulty']['level']
            question['paid_only'] = q['paid_only']
            yield question

    def parse_title_zh(self, response):
        """
        获取翻译
        :param response:
        :return:
        """
        translations = dict()
        data = json.loads(response.text)
        for t in data['data']['translations']:
            translations[int(t['question']['questionId'])] = t['title']
        url = 'https://leetcode-cn.com/api/problems/all/'
        return scrapy.Request(url=url, meta={"translations": translations}, callback=self.parse)
