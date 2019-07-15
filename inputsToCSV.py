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
        header = '%s (%s)' % (item.name, item.kind)
        print(header)
        print('='*len(header))
        content = item.content
        for key in sorted(content.keys()):
            value = content[key]
            print('%s: %s' % (key, value))
        print()


if __name__ == "__main__":
    main()
