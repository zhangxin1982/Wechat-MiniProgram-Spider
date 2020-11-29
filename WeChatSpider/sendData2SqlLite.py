# -*- coding: utf-8 -*-
import pymysql
import json
import os
from apscheduler.schedulers.blocking import BlockingScheduler  # 后台运行
import locationsCut
import  productClass as pcls
import shutil
import  models as db
import datetime
sched = BlockingScheduler()

def readDir(path,strtime):#path 为小程序的目录名字 str time 格式为：2020-11-23
    files = os.listdir(path)

    for f in files:
        if strtime != f:
            continue
        if (os.path.isdir(path + '/' + f)):
            subpath = path + '/' + f
            subfiles = os.listdir(subpath)
            #这里是字符串的对比文件夹名字（分大小写）
            for sf in subfiles:
                with open(subpath+'/'+sf, "r") as readf:  # 打开文件
                    data = readf.read()  # 读取文件
                    if path == "xsyx":
                        try:
                            rowcount = insertWithxsyx(data)
                        except Exception as error:
                            print(error)
                            print(sf)
                    if path ==  "ddmc":
                        try:
                            rowcount = insertWithddmc(data)
                        except Exception as error:
                            print(error)
                            print(sf)
                    if  path == "sht":
                        try:
                            rowcount  = insertWithsht(data)
                        except Exception as error:
                            print(error)
                            print(sf)
                    if path == "mtyx":
                        try:
                            rowcount = insertWithmtyx(data)
                        except Exception as error:
                            print(error)
                            print(sf)

                    if path == "cxyx":
                        try:
                            rowcount = insertWithcxyx(data)
                        except Exception as error:
                            print(error)
                            print(sf)
            # shutil.rmtree(path + '/' + f)

def insertWithcxyx(string): #橙心优选
    jsonobj = json.loads(string)
    time = jsonobj["time"]
    req = jsonobj["req"]
    res = jsonobj["res"]
    cls = jsonobj["class"]
    location = jsonobj["location"]
#分词地址，返回地址编码
    ids = locationsCut.convertLocation2IDS(location)
    procode = ids[0]
    citycode = ids[1]
    areacode = ids[2]

    data = res["data"]
    records = data["result"][0]["goods"]

    if records != None:
        datalist = []
        ids = []
        for obj in records:
            ids.append(str(obj["data"]["id"]))

        #赋值实体对象，这里跟根据情况做数据判断是否重复，本代码是基于商品id判断重复，但实际业务是无需判断重复的
        def updateModel(ml):
            cxyx = ml
            for obj in records:
                row = obj["data"]
                if (str(row["id"])) == str(cxyx.goodNumber):
                    # if time > str(cxyx.time):
                    #     cxyx.surplusCount = abs(int(row["stocks"]) - cxyx.surplusCount)
                    #     cxyx.time = time
                    #     print("cxyx-update")
                    records.remove(obj)
        arraylist = db.session.query(db.CXYX).filter(db.CXYX.goodNumber.in_(ids),db.CXYX.time==time).all()
        for ml in arraylist:
            updateModel(ml)
        # db.session.commit()

        for obj in records:
            row = obj["data"]
            winName =  row["categoryName"]#分类名
            count = int(row["stocks"])#可售库存
            categoryId = row["categoryId"]#分类编号
            # 组合要插入的数据数组
            datalist.append((1, time, citycode, "", categoryId, winName, categoryId, winName,
                             row["id"] ,row["name"], row["thumPic"],
                             row["price"], row["linePrice"],
                             count, 0, 0, 0, 0, 0, 0, 0, procode, areacode, row["id"]))
        if len(datalist):
            # 插入数据库 表明，数组
            runSql("tb_cxyx", datalist)


def insertWithmtyx(string): #美团买菜
    jsonobj = json.loads(string)
    time = jsonobj["time"]
    req = jsonobj["req"]
    res = jsonobj["res"]
    cls = jsonobj["class"]
    location = jsonobj["location"]

    ids = locationsCut.convertLocation2IDSWithFUCKMT(location)
    procode = ids[0]
    citycode = ids[0]
    areacode = ids[0]

    data = res["data"]
    records = data["itemList"]
    poiId = req["poiId"]

    if records != None:
        datalist = []
        ids = []
        for obj in records:
            ids.append(poiId+str(obj["skuId"]))

        def updateModel(ml):
            mtyx = ml
            for obj in records:
                if (poiId+str(obj["skuId"])) == str(mtyx.goodNumber):
                    # if time > str(mtyx.time):
                    #     if obj.get("sales") != None:
                    #         mtyx.time = time
                    #         mtyx.surplusCount = int(obj["sales"]["text"]) - mtyx.surplusCount
                    #         print("mtyx-update")
                    records.remove(obj)

        arraylist = db.session.query(db.MTYX).filter(db.MTYX.goodNumber.in_(ids),db.MTYX.time == time).all()
        for ml in arraylist:
            updateModel(ml)
        # db.session.commit()

        categoryId = req["categoryId"]
        for obj in records:
            winName = pcls.findmtyxClassName(cls["data"]["poiCategories"],categoryId)
            count = 0
            if obj.get("sales") != None :
                count = int(obj["sales"]["text"])
            datalist.append((1, time, citycode, "", categoryId, winName, categoryId, winName,
                             poiId+str(obj["skuId"]), obj["skuTitle"]["text"], obj["picUrl"], obj["sellPrice"]["text"].replace("¥",""), obj["dashPrice"]["text"].replace("¥",""),
                             count, 0, 0, 0, 0, 0, 0, 0, procode, areacode, obj["skuId"]))
        if len(datalist):
            runSql("tb_mtyx", datalist)


def insertWithxsyx(string): #兴盛优选
    jsonobj = json.loads(string)
    time = jsonobj["time"]
    req = jsonobj["req"]
    res = jsonobj["res"]
    cls = jsonobj["class"]
    location  =  jsonobj["location"]

    ids = locationsCut.convertLocation2IDS(location)
    procode = ids[0]
    citycode = ids[1]
    areacode = ids[2]

    data = res["data"]
    records = data["records"]
    if records  != None:
        datalist = []
        ids = []
        for obj in  records:
            ids.append(obj["prId"])

        def updateModel(ml):
            xsyx = ml
            for obj in records:
                if  str(obj["prId"]) == str(xsyx.goodNumber):
                    # if obj["limitQty"] != None:
                    #     if time  > str(xsyx.time):
                    #         xsyx.surplusCount = obj["limitQty"] - xsyx.surplusCount
                    #         xsyx.time = time
                    #         print("update")
                    records.remove(obj)
                    return

        arraylist = db.session.query(db.XSYX).filter(db.XSYX.goodNumber.in_(ids)).all()
        for ml in arraylist:
            updateModel(ml)
        # db.session.commit()

        for obj in records:
            winName = pcls.findxsyxClassName(cls,obj["windowId"])
            datalist.append((1,time,citycode,"",str(req["windowId"]),winName,str(obj["windowId"]),winName,
                             str(obj["prId"]),obj["prName"],obj["imgUrl"],obj["marketAmt"],obj["saleAmt"],
                             obj["limitQty"],0,0,0,0,0,0,0,procode,areacode,obj["sku"]))
        # print(datalist)
        if len(datalist):
            runSql("tb_xsyx",datalist)

def insertWithsht(string): #十荟团
    jsonobj = json.loads(string)
    time = jsonobj["time"]
    req = jsonobj["req"]
    cls = jsonobj["class"]
    res = jsonobj["res"]
    location = jsonobj["location"]
    if len(location) > 0:
        ids = locationsCut.convertLocation2IDS(location)
        procode = ids[0]
        citycode = ids[1]
        areacode = ids[2]

        data = res["data"]
        records = data["grouponMerchandiseList"]
        datalist = []

        ids = []
        for obj in records:
            ids.append(obj["merchandiseid"])

        def updateModel(ml):
            sht = ml
            for obj in records:
                if str(obj["merchandiseid"]) == str(sht.goodNumber):
                    # if obj["quantity"] != None and time > str(sht.time):
                    #     sht.surplusCount = obj["quantity"] - sht.surplusCount
                    #     sht.time = time
                    #     print("update")
                    records.remove(obj)
                    return

        arraylist = db.session.query(db.SHT).filter(db.SHT.goodNumber.in_(ids)).all()
        for ml in arraylist:
            updateModel(ml)
        # db.session.commit()

        for obj in records:
            categoryIdList = obj["categoryIdList"]
            cateId = req["diamondId"]
            catename =  pcls.findshtClassName(cls,cateId)
            datalist.append((2, time, citycode, "", cateId, catename, cateId, catename,
                             str(obj["merchandiseid"]), obj["title"], obj["itemimage"], obj["originprice"],
                             obj["activityprice"],
                             obj["quantity"], 0, 0, 0, 0, 0, 0, 0, procode, areacode, ""))
        if len(datalist):
            runSql("tb_sht", datalist)

def insertWithddmc(string): #多多买菜
    jsonobj = json.loads(string)
    time = jsonobj["time"]
    req = jsonobj["req"]
    res = jsonobj["res"]
    location  =  jsonobj["location"]
    if len(location) > 0:

        ids = locationsCut.convertLocation2IDS(location)
        procode = ids[0]
        citycode = ids[1]
        areacode = ids[2]

        records = res["goods_list"]
        datalist = []

        ids = []
        for obj in records:
            ids.append(obj["goods_id"])

        def updateModel(ml):
            ddmc = ml
            for obj in records:
                if  str(obj["goods_id"]) == str(ddmc.goodNumber):
                    # surplusCount = 0
                    # if ddmc.surplusCount != None:
                    #     surplusCount = int(ddmc.surplusCount)
                    # if obj["quantity"] != None and time > str(ddmc.time):
                    #     count = obj["quantity"] - surplusCount
                    #     ddmc.surplusCount = count
                    #     ddmc.time = time
                    #     print("ddmc-update")
                    records.remove(obj)
                    return

        arraylist = db.session.query(db.DDMC).filter(db.DDMC.goodNumber.in_(ids)).all()
        # print(arraylist)
        for ml in arraylist:
            updateModel(ml)
        # db.session.commit()

        for obj in  records:
            goods_tags =  obj["sku_id"]
            skuid = ""
            if len(goods_tags):
                skuid = str(goods_tags[0])
                list_id = req["list_id"]
                list_name =   pcls.findddmcClassName(jsonobj["class"],list_id)
            count = 0
            if obj["quantity"] != None:
                count = obj["quantity"]
            datalist.append((3,time,citycode,"",list_id,list_name,list_id,list_name,
                             str(obj["goods_id"]),obj["goods_name"],obj["image_url"],obj["price"],obj["market_price"],
                             count,0,0,0,0,0,0,0,procode,areacode,skuid))
        # print(datalist)
        if len(datalist) > 0:
            runSql("tb_ddmc",datalist)

def runSql(table,listData):

        conn = pymysql.connect(
            host='',
            port=3306,
            user='at',
            password='',
            database='',
            charset='utf8'
        )
        cursor = conn.cursor()
        sql = 'insert into '+table+'(appClass,time,cityCode,cityName,classNumber,className,' \
              'subclassNumber,subclassName,goodNumber,goodTitle,imageUrl,price,linePrice,' \
              'surplusCount,restrictionBuyCout,canSaleCount,canSaleCycle,daySalesCount,' \
              'monthSalesCount,sumSalesCount,popularityValues,provinceCode,areaCode,skuCode) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        # sql与listData按索引顺序
        rowcount = cursor.executemany(sql, listData)
        conn.commit()
        cursor.close()
        conn.close()
        # print(rowcount)
        print("%d rows success insert %s "%(rowcount,table))


def wireteData():
    db.session = db.Session()
    readDir("cxyx","2020-11-24")
    readDir("mtyx","2020-11-24")
    readDir("ddmc","2020-11-23")
    readDir("sht", "2020-11-24")
    readDir("xsyx", "2020-11-24")
    db.session.close()
    db.engine.dispose()
#
if __name__ == '__main__':
    wireteData()





