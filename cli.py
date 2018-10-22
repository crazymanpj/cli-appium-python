# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-10-22
# Author:  pangjian

import argparse

parser = argparse.ArgumentParser(description='run testcase for appium test')
parser.add_argument('testfile', type=str, help='testcase file')
args = parser.parse_args()

if args.testfile:
    print('run testcase')
