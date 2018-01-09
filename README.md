# my_spider_play
1.env install.  
use python 3.5 or higher
```
virtualenv virtualenv
source virtualenv/bin/activate
pip install -r requirement.txt
```

2.run run.py code using virtualenv python.  
```
cd my_spider
python run.py
```

3.go to out folder see the result.  


# how to start a scrapy project . 
1.  
```
scrapy startproject [my_spider]
```
• scrapy.cfg 项目的配置信息，主要为Scrapy命令行工具提供一个基础的配置信息。（真正爬虫相关的配置信息在settings.py文件中） 

• items.py 设置数据存储模板，用于结构化数据，如：Django的Model  

• pipelines 数据处理行为，如：一般结构化的数据持久化  

• settings.py 配置文件，如：递归的层数、并发数，延迟下载等  

• spiders 爬虫目录，如：创建文件，编写爬虫规则 . 
