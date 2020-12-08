# analystock
python scrapy csv mongo 股票数据 <br><br><br>

# 简介
将股票数据爬取下来并保存到csv文件中，程序结束后将csv文件导入到mongodb.
<br><br><br>

# 环境
Python 3.6.9<br>
Scrapy 2.4.1
<br><br><br>

# 怎样使用
如果只想保存到`csv`文件里，只需要在`run.sh`里保存下面一行代码即可.
```
scrapy crawl stock
```
<br>

如果也想保存到`mongo`，修改shell脚本里对应`host`即可；如果设置了用户名密码，添加`--username`和`--password`参数。

<br>

如果没有`mongoimport`命令，使用以下命令安装 （`Ubuntu`）:
```
sudo apt install mongo-tools
```

<br>

修改`run.sh`里相关路径.

<br>

运行程序
```
./run.sh
```

<br>


另外，股票的交易时间在周一到周五的9点到15点。可以使用`crontab`命令设置一个周期执行函数爬取每天的数据。使用`crontab -e`命令在文件里添加：
```
5 15 * * 1-5 . /etc/profile;/bin/sh /home/zhaoh/pywork/analystock/run.sh
```
意思是每周一到周五每天下午三点五分爬取一次数据，修改`crontab`相关路径并保存，可使用`crontab -l`查看周期执行函数。
