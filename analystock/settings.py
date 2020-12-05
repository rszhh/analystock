'''
Author: your name
Date: 2020-12-02 16:39:05
LastEditTime: 2020-12-05 11:08:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /analystock/analystock/settings.py
'''
# Scrapy settings for analystock project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'analystock'

SPIDER_MODULES = ['analystock.spiders']
NEWSPIDER_MODULE = 'analystock.spiders'

# mongo
MONGO_HOST = "39.96.85.141"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "spider"  # 库名
#MONGO_COLL = "scrapy"  # collection名
#MONGO_USER = "simple" #用户名
#MONGO_PSW = "test" #用户密码

# 设置随机UA
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
RANDOM_UA_TYPE = "random"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'analystock (+http://www.yourdomain.com)'

# Obey robots.txt rules
# robots.txt规定被爬取站点允许爬虫的范围
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 如果多线程爬取数据，股票的排名会乱
# 加入写入mongo之后仍然会乱
# CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 默认下载延迟，固定每次请求延时2s
# DOWNLOAD_DELAY = 3
# 如果想使用随机延迟，需要修改配置middelware
RANDOM_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'analystock.middlewares.AnalystockSpiderMiddleware': 543,
   # 配置随即下载延迟
   'analystock.middlewares.RandomDelayMiddleware': 150,
   # 设置随机User_Agent
   'analystock.middlewares.RandomUserAgentMiddlware': 100,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'analystock.middlewares.AnalystockDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'analystock.pipelines.AnalystockPipeline': 300,
}

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
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
