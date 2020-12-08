#!/bin/sh
###
 # @Author: your name
 # @Date: 2020-12-05 20:02:42
 # @LastEditTime: 2020-12-08 10:38:05
 # @LastEditors: Please set LastEditors
 # @Description: In User Settings Edit
 # @FilePath: /analystock/analy.sh
### 

. /etc/profile
# source /etc/profile

cd /home/zhaoh/pywork/analystock

/home/zhaoh/.local/bin/scrapy crawl stock

today=$(date +'%Y-%m-%d')

mongoimport --host xx.xx.xx.xxx --port 27017 --db spider --collection stock-data-${today} -f rank,code,name,newpiece,todaymain,todayrank,todaytrend,fivemain,fiverank,fivetrend,tenmain,tenrank,tentrend,plate,platecode --type csv < ./data/stock-data-${today}.csv
