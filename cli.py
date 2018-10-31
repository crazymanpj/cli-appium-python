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

args = parser.parse_args()

Log.set_log_level(args.loglevel)

if args.testfile:
    r = Runner(args.testfile)
    r.runTestCase()
