#!/usr/bin/env python
# coding : utf-8

from __future__ import print_function
import sys
from splunklib.client import connect
from utils import parse


def main():
    opts = parse(sys.argv[1:], {}, ".splunkrc")
    service = connect(**opts.kwargs)

    for item in service.inputs:
        kind = item.kind
        if kind.tolower() == 'rest':
            if 'sourcetype' in item.content and 'description' in item.content:
                if item.content['sourcetype'].tolower() == 'monitoring:webshop':
                    print(item.content['description'])


if __name__ == "__main__":
    main()
