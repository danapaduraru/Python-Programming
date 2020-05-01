import datetime
import hashlib
import os
import re
import sqlite3
import sys
import urllib.request
import zipfile
import json


def problema1(sir):
    count = 0
    for c in sir:
        if c.isdigit():
            count += 1
    return count


def problema2(url):
    r = urllib.request.Request(url)
    response = urllib.request.urlopen(r)
    resp = response.read().decode()
    resp = json.loads(resp)
    count = 0
    for k in resp.keys():
        count += 1
    return count


def problema3(url):
    r = urllib.request.Request(url)
    response = urllib.request.urlopen(r)
    resp = response.read().decode()
    # lis = re.findall('<img src=\".\" alt=\".\" />', resp)
    lis = re.findall('<img src=\".+', resp)
    newlis = []
    for sir in lis:
        sir = sir[sir.index('<img src=\"')+10:sir.rindex('png') + 3]
        newlis.append(sir)
    return newlis


def problema4(my_path):
    hashes = []
    z = zipfile.ZipFile(my_path, 'r')
    for elem in z.namelist():
        with open(elem, 'r') as fd:
            hashes.append(md5(fd.read()).hexdigest())
    return hashes


