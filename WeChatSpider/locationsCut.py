# encoding=utf-8
import jieba
import json
import os


def readLocationJson():
    with open("location.json",'r',encoding="utf-8") as readf:
        data = readf.read()
        res = json.loads(data)
        return res

objlocaiton = readLocationJson()


def convertLocation2IDSWithFUCKMT(locaiton):
    seg_list = jieba.cut(locaiton, cut_all=False)
    strlist = list(seg_list)
    proName = ""
    cityName =""
    areaName =""

    proName = strlist[0]
    cityName = strlist[0]
    areaName = strlist[0]

    ids = findLocationsIdsWithNamesWithFUCKMT(proName)
    # print(ids)
    return ids

def convertLocation2IDS(locaiton):

    if "省" in locaiton:
        seg_list = jieba.cut(locaiton, cut_all=False)
        strlist = list(seg_list)
        proName = ""
        cityName =""
        areaName =""
        #当只有直辖市的时候
        if len(strlist) == 1:#locaiton中与省市区字典匹配后的个数
            proName = strlist[0]
            cityName = strlist[0]
            areaName = strlist[0]
        #当直辖市带区的时候
        if len(strlist) == 2:
            proName=strlist[0]
            cityName=strlist[0]
            areaName=strlist[1]
        #正常省市区的时候
        if len(strlist) >= 3:
            proName = strlist[0]
            cityName = strlist[1]
            areaName = strlist[2]
        ids = findLocationsIdsWithNames(proName,cityName,areaName)
        # print(ids)
        return ids
    else:
        return convertLocation2IDSWithFUCKMT(locaiton)

def findLocationsIdsWithNames(proName,cityName,areaName):

    proid = ""
    cityid = ""
    areaid = ""
    for pro  in objlocaiton:
        if pro["name"] == proName:
            proid = pro["code"]
            for city in pro["cityList"]:
                if city["name"] == cityName:
                    cityid = city["code"]
                    for area in city["areaList"]:
                        if area["name"] == areaName:
                            areaid = area["code"]
                            break
    return [proid,cityid,areaid]

def findLocationsIdsWithNamesWithFUCKMT(cityName):
    proid = ""
    cityid = ""
    areaid = ""
    for pro  in objlocaiton:
        for city in pro["cityList"]:
            if city["name"] == cityName:
                cityid = city["code"]
                break
    return [cityid,cityid,cityid]
