# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-22
# Author:  pangjian

import argparse
from log import Log
from runner import Runner

parser = argparse.ArgumentParser(description='run testcase for appium test')
parser.add_argument('testfile', type=str, help='testcase file')
parser.add_argument('--loglevel', type=str, help='set log level', default='INFO')
parser.add_argument('--no-reset', help='no install apk and reset', default=False, action="store_true")
parser.add_argument('--pertest', help='generate per data', default=False, action="store_true")

args = parser.parse_args()

Log.set_log_level(args.loglevel)

if args.testfile:
    r = Runner(args.testfile)
    r.runTestCase(isnoreset = args.no_reset, ispertest = args.pertest)
