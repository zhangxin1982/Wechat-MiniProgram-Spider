

def findxsyxClassName(obj,wid):
    data = obj["data"]
    windows = data["brandHouseWindows"]
    for window in windows:
        if wid ==  window["brandWindowId"]:
            return window["windowName"]

    for window in data["classifyWindows"]:
        if wid ==  window["windowId"]:
            return window["windowName"]

    for window in data["activityWindows"]:
        if wid ==  window["windowId"]:
            return window["windowName"]

    return ""


def findshtClassName(obj,cid):
    data = obj["data"]

    for window in data:
        if str(cid) ==  str(window["categoryId"]):
            return window["title"]
    return ""



def findddmcClassName(obj,uuid):

    for window in obj:
        if str(uuid) ==  str(window["channel_uuid"]):
            return window["channel_name"]

    return ""


def findmtyxClassName(obj,uuid):

    for window in obj:
        if str(uuid) ==  str(window["id"]):
            return window["name"]
    return ""



