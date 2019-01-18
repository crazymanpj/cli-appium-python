# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-12-04
# Author:  pangjian
from adbhelper import AdbHelper
import threading,time
from lib.mynum import float_decimal2
from log import Log
logger = Log.get_logger(__name__)

class PerTest():

    def __init__(self, packagename):
        self.packagename = packagename
        self.sleeptime = 5
        self.totaltime = 300
        self.datausagetime = 300
        self.cpu_aver = ''
        self.mem_aver = ''
        #rx接收      tx传输
        self.rx_total_mb = ''
        self.tx_total_mb = ''
        self.rx_bytes_s, self.tx_bytes_s = 0,0
        self.rx_bytes_e, self.tx_bytes_e = 0,0

    def startMon(self):
        logger.debug('per start')
        time.sleep(30)
        threads = []
        tcpu = threading.Thread(target=self.threadCpu)
        threads.append(tcpu)
        tmem = threading.Thread(target=self.threadMem)
        threads.append(tmem)
        tdata = threading.Thread(target=self.threadData)
        threads.append(tdata)
        try:
            for t in threads:
                t.daemon = False
                t.start()
                time.sleep(1)
        except Exception as e:
            logger.info(str(e))


    def StopMon(self):
        pass


    def threadCpu(self):
        cpulist = []
        for i in range(0, self.totaltime, self.sleeptime):
            m_cpu = AdbHelper.getCpu(self.packagename)
            if m_cpu:
                m_cpu = m_cpu.strip('%')
                logger.debug(m_cpu)
                cpulist.append(m_cpu)
            time.sleep(self.sleeptime)

        logger.debug(cpulist)
        temp = 0
        for i in cpulist:
            temp = temp + int(i)

        self.cpu_aver = str(float_decimal2(temp / len(cpulist)))
        logger.debug('cpu_aver: ' + self.cpu_aver)

    def threadMem(self):
        memlist = []
        for i in range(0, self.totaltime, self.sleeptime):
            m_memory = AdbHelper.getMemory(self.packagename)
            if m_memory:
                memlist.append(m_memory)
            time.sleep(self.sleeptime)

        temp = 0
        for i in memlist:
            temp = temp + int(i)

        self.mem_aver = str(float_decimal2(temp / len(memlist) / 1024))
        logger.debug('mem_aver: ' + self.mem_aver)

    def threadPower(self):
        pass

    def threadData(self):
        logger.debug('threadData start')
        for i in range(0, self.totaltime, self.sleeptime):
            ret = AdbHelper.getDataUsage(self.packagename)
            if ret is False:
                time.sleep(self.sleeptime)
            else:
                self.rx_bytes_s, self.tx_bytes_s = ret[0], ret[1]
                break

        time.sleep(self.datausagetime)

        for i in range(0, self.totaltime, self.sleeptime):
            ret = AdbHelper.getDataUsage(self.packagename)
            if ret is False:
                time.sleep(self.sleeptime)
            else:
                self.rx_bytes_e, self.tx_bytes_e = ret[0], ret[1]
                break

        self.rx_total_mb = str(float_decimal2((self.rx_bytes_e - self.rx_bytes_s) /1024 /1024))
        self.tx_total_mb = str(float_decimal2((self.tx_bytes_e - self.tx_bytes_s) / 1024 /1024))
