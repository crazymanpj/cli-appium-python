# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-23
# Author:  pangjian
import os, subprocess

PROJECTPATH = os.getcwd()

class AndroidHelper(object):

    def __init__(self):
        pass

    def getApkInfo(self, apkFilePath):
        aaptPath = os.path.join(PROJECTPATH, 'tool', "aapt.exe")
        print(aaptPath)
        if os.path.exists(aaptPath) == 0:
            return
        versioncode = ""
        cmd = aaptPath + " d badging" +" " + apkFilePath
        ret = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
        cmdret = ret.stdout.read()
        print(cmdret)
        cmdret = cmdret.decode('utf-8')
        packageInfo = cmdret.splitlines()[0]
        arraytemp = packageInfo.split(" ")
        for subitem in arraytemp:
            if subitem.find("versionCode") >= 0:
                versioncodeinfo = subitem
                versioncode = versioncodeinfo.split("=")[1].strip("'")
            elif subitem.find("name") >= 0:
                info = subitem
                packagename = info.split("=")[1].strip("'")
        return packagename,versioncode
