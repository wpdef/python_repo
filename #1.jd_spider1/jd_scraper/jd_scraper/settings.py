# Scrapy settings for jd_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "jd_scraper"

SPIDER_MODULES = ["jd_scraper.spiders"]
NEWSPIDER_MODULE = "jd_scraper.spiders"
ROBOTSTXT_OBEY = False
DEFAULT_REQUEST_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Cookie':'__jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1739453919140; mba_muid=1739453919139976805723; mba_sid=17394539191432925787127657646.1; 3AB9D23F7A4B3CSS=jdd03H2WM3JJHM4LLPYNIQZ74HCMXQJ5OBZXGDQNQGLRX6YOXB4DEE3TIWUN73HJDTH4N443SSOYRUUPLHLCGH5FDBDSK4UAAAAMU76EHFYYAAAAADT5VECTMX3SNRQX; _gia_d=1; wlfstk_smdl=1xb7enofhq9sqf13z9xjotv6hf00xlbz; __jdu=1739453919139976805723; TrackID=1Zzd-GkfUlyDqjmcZWjHjgczRoC9L60NsRJ6-ZlvEgm68MP3qJshzfu5z8HyE3yRuAq_Jan_ErezF4CWTr65ZRzQQnsy1rMQ6v5330enR6C0; thor=FFC264252E62EA92743718F58BA29C5390A41E9E586F68CAE937C2C9B05C2CDDBC280325E77EA703138256622A7A183B15F1D5850F96B8F51E4C47D623B57DF866D71D0B6DFEB0A61E9A7D76B2FF155D9CD7507AE856F1EC66F7030317B1BBF09707BB45FC9E2975F5968EA5FE0FB50AC7407B872427BBDD845AC0AF50EDF41E0705071AE5664C56F4BE53F4E3411E61; light_key=AASBKE7rOxgWQziEhC_QY6ya54jGyyTei2jv23F8b42VWqH08p-doi172z1ZCfVEqW2u24jM; pinId=jsSpVomLMkB4-qPS9PNQiQ; pin=18500425520_p; unick=jd185004lts; ceshi3.com=000; _tp=bQoH%2FMqFIumGj5jZ0Q0qXg%3D%3D; _pst=18500425520_p; ipLoc-djd=13-1000-0-0; __jda=29846306.1739453919139976805723.1739453919.1739453919.1739453919.1; __jdc=29846306; jsavif=1; jsavif=1; xapieid=jdd03H2WM3JJHM4LLPYNIQZ74HCMXQJ5OBZXGDQNQGLRX6YOXB4DEE3TIWUN73HJDTH4N443SSOYRUUPLHLCGH5FDBDSK4UAAAAMU76EHFYYAAAAADT5VECTMX3SNRQX; __jdb=29846306.4.1739453919139976805723|1.1739453919; flash=3_jrLxBytlxd7Thers8YtUAL1ocpdtHYZjh5viSWCAmYG-jm4xGQahDmGqMaHma2Wd-a6bj5edTvUV2H6hGUnxeoSznWpnHRH-3KKF87XbdauRwbFF6uBsjzyisaHhdy-npBbhnfdA0jE6QWwXm7rnh_jgEx4Wgok37sOFCXl3ZiZijcCKRq**; shshshfpa=35d15c7f-cb3b-7a6f-012f-c5b0075cc581-1739453951; shshshfpx=35d15c7f-cb3b-7a6f-012f-c5b0075cc581-1739453951; areaId=13; shshshfpb=BApXSWGWA_PFAJ_JvOXyU27PmrMe8mnRbBnsEPn5o9xJ1Mr3NsIG2; 3AB9D23F7A4B3C9B=H2WM3JJHM4LLPYNIQZ74HCMXQJ5OBZXGDQNQGLRX6YOXB4DEE3TIWUN73HJDTH4N443SSOYRUUPLHLCGH5FDBDSK4U',

}
RETRY_TIMES = 5
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "jd_scraper (+http://www.yourdomain.com)"

# Obey robots.txt rules


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "jd_scraper.middlewares.JdScraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "jd_scraper.middlewares.JdScraperDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "jd_scraper.pipelines.JdScraperPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
