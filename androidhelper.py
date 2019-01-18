# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-23
# Author:  pangjian
import os, subprocess, re
from log import Log
from lib.mystr import getstrencodingtype
from const import SYSTEM


PROJECTPATH = os.getcwd()
logger = Log.get_logger(__name__)
logger.debug(__name__)

class AndroidHelper(object):

    def __init__(self, apkFilePath):
        logger.debug(apkFilePath)
        logger.debug(os.getcwd())
        self.apkfilepath = apkFilePath
        self.packagename = ''
        self.versioncode = ''
        self.appActivity = ''
        self.getApkInfo()

    def getApkInfo(self):
        packagename = ''
        if SYSTEM == 'Windows':
            aaptPath = os.path.join(PROJECTPATH, 'tool', "aapt.exe")
        elif SYSTEM == 'Linux':
            aaptPath = 'aapt'
        else:
            return False

        if SYSTEM == 'Windows' and os.path.exists(aaptPath) == 0:
            return False

        versioncode = ""
        cmd = aaptPath + " d badging" +" " + self.apkfilepath
        logger.debug(cmd)
        if SYSTEM == 'Windows':
            ret = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
        elif SYSTEM == 'Linux':
            ret = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
        else:
            return False
        cmdret = ret.stdout.read()
        logger.debug(cmdret)
        logger.debug(getstrencodingtype(cmdret))
        try:
            cmdret = cmdret.decode(getstrencodingtype(cmdret))
        except Exception as e:
            logger.error(str(e))

        packageInfos = cmdret.splitlines()
        if SYSTEM == 'Windows':
            packageInfos = str(packageInfos)
        logger.debug(packageInfos)
        logger.debug(type(packageInfos))
        for i in packageInfos:
            logger.debug(i)
            if i.find(u'launchable-activity') >= 0:
                pattern = r"launchable-activity: name='(\S+)'"
                m = re.match(pattern, i)
                self.appActivity = m.group(1)
                logger.debug('self.appActivity: ' + self.appActivity)
        arraytemp = packageInfos[0].split(" ")
        logger.debug('arraytemp: ')
        logger.debug(arraytemp)
        for subitem in arraytemp:
            if subitem.find("versionCode") >= 0:
                versioncodeinfo = subitem
                versioncode = versioncodeinfo.split("=")[1].strip("'")
                logger.debug('versionCode: ' + versioncode)

            pattern = r"name='(\S+)'"
            m = re.match(pattern, subitem)
            if m:
                packagename = m.group(1)
                logger.debug('packagename: ' + packagename)

        self.packagename = packagename
        self.versioncode = versioncode
