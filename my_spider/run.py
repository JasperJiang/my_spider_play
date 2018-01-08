# -*- coding: utf-8 -*-

from scrapy import cmdline


name = 'MySpider'
cmd = 'scrapy crawl {0} --nolog'.format(name)
cmdline.execute(cmd.split())