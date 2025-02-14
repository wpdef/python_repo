##1.安裝 scrapy:
pip install scrapy
##2.代码部分省略……

##3.当无法正常爬取数据时请更换网站headers

##运行项目并导出json数据
scrapy crawl jd -o goods.json -t json
