# -*- coding: utf-8 -*-

import urllib.request

import urllib3

def conn_check(url, only200):
    global pathlist
    global CodeError
    global Exept
    pathlist = []
    CodeError = []
    Exept = "NOT"
    salida = 1
    try:
        for line in urllib.request.urlopen("http://" + url + "/robots.txt"):
            lineStr = str(line, encoding='utf8')
            path = lineStr.split(': /')
            if "Disallow" == path[0]:
                pathlist.append(path[1].replace("\n", "").replace("\r", ""))
                pathlist = list(set(pathlist))
            try:
                inx = pathlist.index("/")
                del pathlist[inx]
            except:
                pass
    except urllib.error.HTTPError:
        Exept = ("\n" + "No robots.txt file has been found.")
        salida = 0
        return salida, Exept, pathlist, CodeError
    except urllib.error.URLError:
        Exept = ("\n" + "Please, type a valid URL. This URL can't be resolved." )
        salida = 0
        return salida, Exept, pathlist, CodeError

    http = urllib3.PoolManager()
    count = 0
    count_ok = 0

    for p in pathlist:
        disurl = "http://" + url + '/' + p
        r1 = http.request('GET', disurl, redirect=False, retries=5)
        if r1.status == 200:
            CodeError.append(str(r1.status) + ' ' + str(r1.reason))
            count_ok = count_ok + 1

        elif only200 == False:
            CodeError.append(str(r1.status) + ' ' + str(r1.reason))
        count = count + 1
    count_ok_int = int(count_ok)

    if salida == 1:
        if count_ok_int != 0 and only200 == True:
            pass
        elif count_ok_int != 0:
            pass
        elif count_ok_int == 0 and only200 == True:
            pass
        else:
            pass
    return salida, Exept, pathlist, CodeError

def search_yandex(url, search, only200):
    from bs4 import BeautifulSoup
    Data = []
    Err=""
    count = 0
    for p in pathlist:
        disurl = "http://" + url + '/' + p
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0')]
        url2 = "http://www.yandex.ru/search?q=site:" + disurl
        Data.append(url2)
        page = opener.open(url2)
        soup = BeautifulSoup(page)
        http = urllib3.PoolManager()
        for cite in soup.findAll('cite'):
            try:
                if url in cite.text:
                    count = count + 1
                    r2 = http.request('GET', cite.text, redirect=False, retries=5)
                    if r2.status == 200:
                        Data.append(' - ' + cite.text + ' ' + str(r2.status) + ' ' + str(r2.reason))
                    elif only200 == False:
                        Data.append(' - ' + cite.text + ' ' + str(r2.status) + ' ' + str(r2.reason))
            except UnicodeEncodeError:
                pass
    if count == 0:
        Err = ('No Dissallows have been indexed in Yandex' )

    return Data, Err, count




