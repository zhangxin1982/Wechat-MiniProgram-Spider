# -*- coding: utf-8 -*-
import mitmproxy.http
from mitmproxy import ctx
import time
import json
import uuid
import os
from urllib import parse

class Counter:
    def __init__(self):
        self.num = 0
        self.requestNum = 0
        self.responseOrErrorNum = 0
        self.aa = 0
        self.xsyxlocation = ""
        self.shtlocaiton = ""
        self.ddmclocation = ""
        self.mtyxlocation = ""
        self.mtyxaddress = ""
        self.cxyxlocation = ""

        self.xsyxClassJson =""
        self.ddmcClassJson  = ""
        self.shtClassJson = ""
        self.mtyxClassJson = ""
        self.cxyxClassJson = ""

    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        pass
        # flow.customField = []

    def request(self, flow: mitmproxy.http.HTTPFlow):
        self.num = self.num + 1
        self.requestNum = self.requestNum + 1
        flow.start_time = time.time()
        # if flow.request.method == "CONNECT":
        #     # If the decision is done by domain, one could also modify the server address here.
        #     # We do it after CONNECT here to have the request data available as well.
        #     client_ip = flow.client_conn.address[0]
        #     # if 'google' in flow.request.url:
        #     #     ctx.log.info(flow.request.url)
        #     #     proxy = ("localhost", 8118)
        #     # else:
        #     #     proxy = ("localhost", 8888)
        # 这里配置二级代理的ip地址和端口
        # if flow.live:
        #     proxy = ("localhost", 8118)
        #     flow.live.change_upstream_proxy_server(proxy)

    def error(self, flow):
        self.aa = self.aa + 1
        self.responseOrErrorNum = self.responseOrErrorNum + 1
        # flow.customField.append("Error response")


    def proectClass(self,flow):
        #	https://mall.xsyxsc.com/user/product/indexWindows
        if flow.request.url == "https://mall.xsyxsc.com/user/product/indexWindows":  # 兴盛优选
            if len(flow.response.text) > 0:
                self.xsyxClassJson = flow.response.text

        if flow.request.url ==  "https://api.nicetuan.net/mc/groupClassify/v3/categoryList": #十荟团
            if len(flow.response.text) > 0:
                self.shtClassJson  = flow.response.text
        # https://bi-mall.meituan.com/api/c/poi/10873579/sku/list/category/42535/v4?uuid=175b74ac60ac8-223351226167cc-0-3d10d-175b74ac60ac8&utm_medium=wxapp&brand=meituanyouxuan&tenantId=1&homepageLng=114.19700622558594&homepageLat=30.546398162841797&utm_term=5
        if "bi-mall.meituan.com/api/c/poi" in flow.request.url and "category/list/v4" in flow.request.url: #美团优选
            if len(flow.response.text) > 0:
                self.mtyxClassJson = flow.response.text
        # https://bi-mall.meituan.com/api/c/poi/10005482/category/list/v4?
        if "yx.zxwcbj.com/route/j/shopGoodsCategory" in flow.request.url:  #橙心优选
            if len(flow.response.text) > 0:
                self.cxyxClassJson = flow.response.text

    def location(self,flow):
        if  flow.request.url == "https://mall-store.xsyxsc.com/mall-store/store/getStoreInfo": #兴盛优选
            if len(flow.response.text) > 0:
                res = json.loads(flow.response.text)
                self.xsyxlocation = res["data"]["detailAddress"]

        if  flow.request.url == "https://api.pinduoduo.com/api/mc/v0/alexa/query_default_store": #拼多多
            if len(flow.response.text) > 0:
                res = json.loads(flow.response.text)
                self.ddmclocation = res["store_info"]["address"]
                self.ddmcClassJson = json.dumps(res["mc_goods_channel_list"])

        if flow.request.url == "https://api.nicetuan.net/index/getPartnerInfo":  # 十荟团
            if len(flow.response.text) > 0:
                res = json.loads(flow.response.text)
                self.shtlocaiton = res["data"]["residentialname"]

            #https://bi-mall.meituan.com/api/c/grocerylbs/location
        if "bi-mall.meituan.com/api/c/grocerylbs/location" in flow.request.url: #美团优选
            if len(flow.response.text) > 0:
                # res = json.loads(flow.response.text)
                #{code:0,data:{cityName:武汉市,cityId:16,address:万科汉阳国际,inServiceArea:true}}
                res = json.loads(flow.response.text)
                self.mtyxlocation = res["data"]["targetPoiInfo"]["address"]

        if "https://yx.zxwcbj.com/getShopTuanInfos" in flow.request.url:
            if len(flow.response.text) > 0:
                res = json.loads(flow.response.text)
                curLeaderInfo = res["data"]["curLeaderInfo"]
                self.cxyxlocation = curLeaderInfo["addr"]

    def goodsList(self,flow):
        if flow.request.url == "https://mall.xsyxsc.com/user/window/getProducts/v3": #兴盛优选

            if len(self.xsyxlocation) > 0:
                timeDir = time.strftime("%Y-%m-%d", time.localtime())

                if not os.path.exists("xsyx"):
                    os.makedirs("xsyx")

                dirPath = "xsyx/"+timeDir
                if not os.path.exists(dirPath):
                    os.makedirs(dirPath)
                f  = dirPath+"/"+str(uuid.uuid4())+".txt"
                self.writeTxt(flow.request.text,flow.response.text,self.xsyxlocation,self.xsyxClassJson,f,flow.request.url)

        if flow.request.url == "https://api.pinduoduo.com/api/mc/v0/alexa/goods_list":# 多多买菜
            if len(self.ddmclocation) > 0:
                timeDir = time.strftime("%Y-%m-%d", time.localtime())
                dirPath = "ddmc/" + timeDir

                if not os.path.exists("ddmc"):
                    os.makedirs("ddmc")

                if not os.path.exists(dirPath):
                    os.makedirs(dirPath)
                f = dirPath + "/" + str(uuid.uuid4()) + ".txt"
                self.writeTxt(flow.request.text, flow.response.text,self.ddmclocation ,self.ddmcClassJson,f,flow.request.url)

        if flow.request.url == "https://api.nicetuan.net/mc/diamondV2/list-merchandise":  # 十荟团
            if len(self.shtlocaiton) >  0 :
                timeDir = time.strftime("%Y-%m-%d", time.localtime())

                if not os.path.exists("sht"):
                    os.makedirs("sht")

                dirPath = "sht/" + timeDir
                if not os.path.exists(dirPath):
                    os.makedirs(dirPath)
                f = dirPath + "/" + str(uuid.uuid4()) + ".txt"
                self.writeTxt(flow.request.text, flow.response.text, self.shtlocaiton,self.shtClassJson,f,flow.request.url)

        if "bi-mall.meituan.com" in flow.request.url and "sku/list/category/" in flow.request.url: #美团优选
            if len(self.mtyxlocation) > 0:
                timeDir = time.strftime("%Y-%m-%d", time.localtime())

                if not os.path.exists("mtyx"):
                    os.makedirs("mtyx")

                dirPath = "mtyx/" + timeDir
                if not os.path.exists(dirPath):
                    os.makedirs(dirPath)
                f = dirPath + "/" + str(uuid.uuid4()) + ".txt"
                res = dict(parse.parse_qsl(flow.request.url))
                reqjsonstr = json.dumps(res)
                self.writeTxt(reqjsonstr, flow.response.text, self.mtyxlocation, self.mtyxClassJson, f,flow.request.url)

        if "yx.zxwcbj.com/route/j/shopGoods" in flow.request.url:
            if len(self.cxyxlocation) > 0:
                timeDir = time.strftime("%Y-%m-%d", time.localtime())

                if not os.path.exists("cxyx"):
                    os.makedirs("cxyx")

                dirPath = "cxyx/" + timeDir
                if not os.path.exists(dirPath):
                    os.makedirs(dirPath)
                f = dirPath + "/" + str(uuid.uuid4()) + ".txt"
                res = dict(parse.parse_qsl(flow.request.url))
                reqjsonstr = json.dumps(res)
                self.writeTxt(reqjsonstr, flow.response.text, self.cxyxlocation, self.cxyxClassJson, f,flow.request.url)


    def response(self, flow):
        self.aa = self.aa + 1
        self.responseOrErrorNum = self.responseOrErrorNum + 1
        flow.end_time = time.time()
        self.location(flow)
        self.proectClass(flow)
        self.goodsList(flow)


    def writeTxt(self,reqText,resText,location,classjson,f,urlstr):
        with open(f, "w") as file:
            req = json.loads(reqText)
            res = json.loads(resText)
            cls = json.loads(classjson)
            timeString = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            dict = {"time": timeString, "location":location ,"class":cls,"req": req, "res": res,"url":urlstr}
            jsonstr = json.dumps(dict)
            file.write(jsonstr)


addons = [
    Counter()
]
