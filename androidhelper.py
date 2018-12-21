# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-23
# Author:  pangjian
import os, subprocess, re
from log import Log
logger = Log.get_logger(__name__)
from lib.mystr import getstrencodingtype

PROJECTPATH = os.getcwd()

class AndroidHelper(object):

    def __init__(self, apkFilePath):
        self.apkfilepath = apkFilePath
        self.packagename = ''
        self.versioncode = ''
        self.appActivity = ''
        self.getApkInfo()

    def getApkInfo(self):
        aaptPath = os.path.join(PROJECTPATH, 'tool', "aapt.exe")
        if os.path.exists(aaptPath) == 0:
            return
        versioncode = ""
        cmd = aaptPath + " d badging" +" " + self.apkfilepath
        ret = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
        cmdret = ret.stdout.read()
        logger.debug(cmdret)
        logger.debug(getstrencodingtype(cmdret))
        try:
            cmdret = cmdret.decode(getstrencodingtype(cmdret))
        except Exception as e:
            logger.error(str(e))

        packageInfos = cmdret.splitlines()
        for i in packageInfos:
            if i.find(u'launchable-activity') >= 0:
                pattern = r"launchable-activity: name='(\S+)'"
                m = re.match(pattern, i)
                self.appActivity = m.group(1)
        arraytemp = packageInfos[0].split(" ")
        for subitem in arraytemp:
            if subitem.find("versionCode") >= 0:
                versioncodeinfo = subitem
                versioncode = versioncodeinfo.split("=")[1].strip("'")
            elif subitem.find("name") >= 0:
                info = subitem
                packagename = info.split("=")[1].strip("'")
        self.packagename = packagename
        self.versioncode = versioncode
