#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

delims = [
    "，", "。", "；", "：", "！",
    "?", "？", ";", ":", "!",
    ",", ".", "\"", "'", "“",
    "‘", "’", "(", ")", "”",
    "（", "）", "%", "％", "@",
    "~", "`", "～", "｀", "#",
    "、", "/", "\\", "<", ">",
    "《", "》", "／", "｛", "｝",
    "{", "}", "[", "]", "［",
    "］", "|", "｜", "\n", "\r",
    " ", "\t", "　"
    ]\
    + list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")\
    + list("abcdefghijklmnopqrstuvwxyz")\
    + list("0123456789")
