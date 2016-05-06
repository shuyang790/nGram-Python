# nGram-Python
nGram: New Word Recognition (Chinese news texts).

This repo contains **dataCollector** (which crawls data from Sina news website), **dataCleaner** (which tidies the crawled data and aggregates them), **nGram** (which counts n-gram words and produce nGram data), and **wordRecognition** (which uses the nGram data to recognize chinese words).

## Code Constitution Specifics

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


## Data Specifics

The raw data is acquired by `dataCollector` and classified by date.
The data contain Sina news texts with labels like `<p></p>`, and the Cinese-text-only result
is acquired by `dataCleaner` as `data.txt` (using texts of 2006 January - April, totally
`1.9GB` approximately, `1,990,660,672 bytes` precisely).
