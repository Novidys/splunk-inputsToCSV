#!/usr/bin/env python
# coding : utf-8

from __future__ import print_function
import sys
from splunklib.client import connect
from utils import parse


HEADER = 'Description, Endpoint, State, Index, Sourcetype'
def main():
    opts = parse(sys.argv[1:], {}, ".splunkrc")
    service = connect(**opts.kwargs)

    print(HEADER)

    for item in service.inputs:
        if item.kind.lower() == 'rest':
            if 'sourcetype' in item.content and 'description' in item.content and 'disabled' in item.content and \
                    'endpoint' in item.content and 'index' in item.content:
                print('"%s","%s","%s","%s","%s"' % (item.content['description'], item.content['endpoint'],
                                          item.content['disabled'], item.content['index'], item.content['sourcetype']))


if __name__ == "__main__":
    main()
