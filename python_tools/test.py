#! /usr/bin/python
#encoding:gb18030

from string_process import strB2Q
from string_process import strQ2B
import sys

if __name__ == '__main__':

    ustring = sys.argv[1].decode('gb18030')
    print strB2Q(ustring).encode('gb18030')
    print strQ2B(ustring).encode('gb18030')

