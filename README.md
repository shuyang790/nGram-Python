# nGram-Python
nGram: New Word Recognition (Chinese news texts).

This repo contains **dataCollector** (which crawls data from Sina news website), **dataCleaner** (which tidies the crawled data and aggregates them), **nGram** (which counts n-gram words and produce nGram data), and **wordRecognition** (which uses the nGram data to recognize chinese words).

## Constitution Specifics

### dataCollector

Spiders to crawl Sina news texts (with titles), using Python's _Requests_ + _BeautifulSoup_.

Data source:
From daily news list "http://news.sina.com.cn/old1000/news1000_YYYYMMDD.shtml", where `YYYY`, `MM`, `DD` are year, month, and day respectively.

### dataCleaner

Python script to aggregate the crawled texts in a year to a single file, e.g. `2006_all`.

### nGram

Scan texts to generate statistical nGram files.

### wordRecognition

Use nGram data to recognize words.


## Results

### Text data
