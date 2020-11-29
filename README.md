# MiniProgram-Spider  
通过mitmproxy,对微信团购小程序抓包。获取商品列表数据写入数据库  

## 常规方式要求有 Python 环境，安装具体要求如下： 
Python>=3.6   
pip3 install mitmproxy pip3  
install pymysql  
pip3 install sqlalchemy   
pip3 insatll jieba  
pip3 insatll apscheduler  

## 运行步骤如下:  
git clone https://github.com/zhangxin1982/MiniProgram-Spider.git  
cd MiniProgram-Spider/WeChatSpider  
mkdir xsyx && mkdir mtyx && mkdir ddmc && mkdir sht && mkdir cxyx  
python3 main.py  

这时 mitmproxy 已经运行。默认端口是 8080  

## 抓取操作步骤如下:
### 用iPhone 打开 safari 输入 mitm.it ,下载cer证书。安装证书，设置证书信任。  
### 参考地址:https://medium.com/testvagrant/intercept-ios-android-network-calls-using-mitmproxy-4d3c94831f62  

### 打开微信小程序，以美团优选 为例子:  
#### 点击我的 切换站点 (必须做这一步，列表数据是根据地址来对应的，没有地址数据不会写入) 其他的小程序以此类推  
#### 滑动商品列表，获取数据(此时已经写入到根目录下的mtyx文件夹,文件是通过txt的方式存储)  

## 写入数据库:

### 需要一个mysql，执行sql目录下的 建表脚本。（关于mysql 这里不在累赘）  
### 修改 sendData2SqlLite.py 和 models 文件 里面的 你自己的mysql连接地址，账号，密码  
### 运行 python3 sendData2SqlLite.py  （控制输出 sucess rowscount 就说明插入成功）  

## 外网部署 阿里云示例:
1 阿里云 ubuntu 18.04,安装python 依赖环境。与上同理  
2 部署代码到阿里云 进入目录。执行: mitmdump -p 8888  --set block_global=false -s addons.py  
3 您的设备可以在外网的环境 设置阿里云的IP 和 上面命令运行的端口。就可以实现外网抓取小程序。


以上代码仅仅供参考学习，如有其他问题或者有其他更好的解决方案，请加 qq:8772037 讨论。








