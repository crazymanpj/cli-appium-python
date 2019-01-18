# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-22
# Author:  pangjian

import argparse,subprocess,os
from log import Log
from runner import Runner
from log import Log
import traceback
logger = Log.get_logger(__name__)
PROJECTPATH = os.getcwd()

parser = argparse.ArgumentParser(description='run testcase for appium test')
parser.add_argument('testset', type=str, help='testcase dir or set')
parser.add_argument('--loglevel', type=str, help='set log level', default='INFO')
parser.add_argument('--no-reset', help='no install apk and reset', default=False, action="store_true")
parser.add_argument('--pertest', help='generate per data', default=False, action="store_true")
parser.add_argument('--monkeyrunner', type=str, help='run the configfile with monkeyrunner', dest='mrconfile')

args = parser.parse_args()


Log.set_log_level(args.loglevel)

logger.info(args)
if args.mrconfile:
    mymonkeyfile = os.path.join(os.getcwd(), 'mymonkeyrunner.py')
    configfile = os.path.join(os.getcwd(), args.mrconfile)
    logger.info(mymonkeyfile)
    logger.info(configfile)
    cmd = 'monkeyrunner' + ' ' +  mymonkeyfile + ' ' + configfile + ' ' + PROJECTPATH
    logger.info(cmd)
    subp = subprocess.Popen(cmd, shell=True)
    subp.wait()
    subp.kill()
    sys.exit(0)

try:
    logger.debug('start')
    if args.testset:
        r = Runner(args.testset)
        r.runTestCase(isnoreset = args.no_reset, ispertest = args.pertest)
except Exception as e:
    logger.info(traceback.format_exc())
    logger.error("%s exception !!!  msg: %s"%(r.exception_define, str(e)))
