# -*- coding:utf-8 -*-
from pyquery import PyQuery as pq
import requests
import re
import json


class Translate(object):
    def __init__(self):
        self.result_e = {"aiciba_e": {"content":"","url":""}, "haiciwang_e":  {"content":"","url":""}, "ciduwang_e":  {"content":"","url":""}, "gugefanyi_e":  {"content":"","url":""}}
        self.result_j = {"bzd1_j": {"content":"","url":""}, "huajiang_j":  {"content":"","url":""}, "yahu_j":  {"content":"","url":""}, "bzd2_j":  {"content":"","url":""}, "gugefanyi_j":  {"content":"","url":""}}

    def translation_e(self, text):
        url = u"http://www.iciba.com/" + text
        d = pq(url)
        self.result_e["aiciba_e"]["content"] = d("body > div.screen > div.container > div.container-left > div.js-base-info > div > div > ul > li").text()
        self.result_e["aiciba_e"]["url"] = url

        url = u"http://juhai.dict.cn/" + text
        d = pq(url)
        self.result_e["haiciwang_e"]["content"] = d(
            "#main > div.juhai > div.adv > div.juhai-syfbt > div.juhai-dict-sy > ul > li").text().encode('latin1').decode('utf8')

        self.result_e["haiciwang_e"]["url"] =url

        url = u"http://www.dictall.com/dictall/result.jsp?cd=UTF-8&keyword=" + text
        d = pq(url)
        pattern = r"createPlayer.*?\);"
        self.result_e["ciduwang_e"]["content"] = re.sub(pattern, "", d(".wordlist").text().split(u"更多例句>>")[0], count=0, flags=0)
        self.result_e["ciduwang_e"]["url"] =url

        if self.check_contain_chinese(text):
            url =   u"https://translate.google.cn/translate_a/single?client=gtk&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=btn&ssel=5&tsel=5&kc=0&tk=819752.708957&q="+text
            r = requests.get(url)
            try:
                self.result_e["gugefanyi_e"]["content"] = json.loads(r.text)[0][0][0]
            except ValueError:
                self.result_e["gugefanyi_e"]["content"] = "谷歌翻译挂了！"
            self.result_e["gugefanyi_e"]["url"] =url
        else:
            url =  u"https://translate.google.cn/translate_a/single?client=gtk&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&swap=1&source=btn&ssel=5&tsel=5&kc=0&tk=135226.279375&q="+text

            r = requests.get(url)
            try:
                self.result_e["gugefanyi_e"]["content"] = json.loads(r.text)[0][0][0]
            except ValueError:
                self.result_e["gugefanyi_e"]["content"] = "谷歌翻译挂了！"
            self.result_e["gugefanyi_e"]["url"] =url

        return self.result_e

    def translation_j(self, text):
        url = u"http://ejje.weblio.jp/" + text
        d = pq(url)
        self.result_e["bzd1_j"]["content"] = d("#headword_jp_1").text()
        self.result_e["bzd1_j"]["url"] = url

        url = u"http://dict.hjenglish.com/jp/jc/" + text
        d = pq(url)
        self.result_e["hujiang_j"]["content"] = d("headword_jp_1").text()
        self.result_e["hujiang_j"]["url"] =url

        url = u"https://dic.yahoo.co.jp/search/?p=%s&ei=UTF-8&fr=top_ga1_sa" %text
        d = pq(url)
        pattern = r"createPlayer.*?\);"
        self.result_e["ciduwang_e"]["content"] = re.sub(pattern, "", d(".wordlist").text().split(u"更多例句>>")[0], count=0, flags=0)
        self.result_e["ciduwang_e"]["url"] =url


        if self.check_contain_chinese(text):
            url =   u"https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=btn&ssel=5&tsel=5&kc=0&tk=819752.708957&q="+text
            r = requests.get(url)
            try:
                self.result_e["gugefanyi_e"]["content"] = json.loads(r.text)[0][0][0]
            except ValueError:
                self.result_e["gugefanyi_e"]["content"] = "谷歌翻译挂了！"
            self.result_e["gugefanyi_e"]["url"] =url
        else:
            url =  u"https://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&swap=1&source=btn&ssel=5&tsel=5&kc=0&tk=135226.279375&q="+text

            r = requests.get(url)
            try:
                self.result_e["gugefanyi_e"]["content"] = json.loads(r.text)[0][0][0]
            except ValueError:
                self.result_e["gugefanyi_e"]["content"] = "谷歌翻译挂了！"
            self.result_e["gugefanyi_e"]["url"] =url

        return self.result_e

    def check_contain_chinese(self, check_str):
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

# trans = Translate()
# trans.translation_e("apple")