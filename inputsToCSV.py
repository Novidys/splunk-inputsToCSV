#!/usr/bin/env python
# coding : utf-8

from __future__ import print_function
import sys
from splunklib.client import connect
from utils import parse


def main():
    opts = parse(sys.argv[1:], {}, ".splunkrc")
    service = connect(**opts.kwargs)
    print('Description')
    for item in service.inputs:
        if item.kind.lower() == 'rest':
            if 'sourcetype' in item.content and 'description' in item.content and 'disabled' in item.content:
                if item.content['sourcetype'].lower() == 'monitoring:webshop':
                    if item.content['disabled'] == '0':
                        print(item.content['description'])


if __name__ == "__main__":
    main()
