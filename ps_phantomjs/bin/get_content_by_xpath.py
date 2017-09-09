#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

from ps_phantomjs import lib


def out_file(url, xpath, path):
    driver = lib.ff_automation()

    driver.start_phantomjs(url)

    title = driver.get_title()
    content_list = driver.get_content_by_xpath(xpath)

    driver.set_content(path, title + '\n')

    for content in content_list:
        driver.add_content(path, content + '\n')

    driver.stop_phantomjs()


def main():
    parser = argparse.ArgumentParser(
        description="""Web ページからテキストを取得し、
                ファイルへ出力します。""")

    parser.add_argument(
        'url',
        help='テキストを取得する Web ページの URL 。')
    parser.add_argument(
        'xpath',
        help='テキストを取得する Web ページ内の要素の XPath。')
    parser.add_argument(
        'path',
        help='取得したテキストを出力するファイルのパス。')

    args = parser.parse_args()

    out_file(args.url, args.xpath, args.path)

if __name__ == '__main__':
    main()
