from scrapy import  cmdline

# cmdline.execute("scrapy crawl cangku -o cangku.csv".split())
cmdline.execute("scrapy crawl content -o content.csv".split())