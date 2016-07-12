#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

from ps_phantomjs import lib


def main():
    parser = argparse.ArgumentParser(
        description="""Web ページからリンクを取得し、
                [label]
                href
                の形式でファイルへ出力します。""")

    parser.add_argument(
        'url',
        help='リンクを取得する Web ページの URL 。')
    parser.add_argument(
        'path',
        help='リンクの情報を出力するファイルのパス。')

    args = parser.parse_args()
    driver = lib.pjs_automation()
    driver.get_links(args.url, args.path)

if __name__ == '__main__':
    main()
