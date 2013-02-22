#! /usr/bin/python
#encoding:gb18030

import sys

def strQ2B(ustring):
    """把字符串全角转半角

    strQ2B("ｉｗｅｎｔａｏ李文涛".decode('gb18030'))
    """
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if inside_code < 0x0020 or inside_code > 0x7e:      #转完之后不是半角字符则返回原来的字符
            rstring += uchar
        else:
            rstring += unichr(inside_code)
    return rstring

def strB2Q(ustring):
    """把字符串半角转全角

    strB2Q("liwentao李文涛".decode('gb18030'))
    """
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code < 0x0020 or inside_code > 0x7e:      #不是半角字符则返回原来的字符
            rstring += uchar
            continue
        if inside_code == 0x0020: #除了空格其他的全角半角的公式为:半角=全角-0xfee0
            inside_code = 0x3000
        else:
            inside_code += 0xfee0
        rstring += unichr(inside_code)
    return rstring

if __name__ == '__main__':

    pass
