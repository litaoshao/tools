#! /usr/bin/python
#encoding:gb18030

import sys

def strQ2B(ustring):
    """���ַ���ȫ��ת���

    strQ2B("����������������".decode('gb18030'))
    """
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if inside_code < 0x0020 or inside_code > 0x7e:      #ת��֮���ǰ���ַ��򷵻�ԭ�����ַ�
            rstring += uchar
        else:
            rstring += unichr(inside_code)
    return rstring

def strB2Q(ustring):
    """���ַ������תȫ��

    strB2Q("liwentao������".decode('gb18030'))
    """
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code < 0x0020 or inside_code > 0x7e:      #���ǰ���ַ��򷵻�ԭ�����ַ�
            rstring += uchar
            continue
        if inside_code == 0x0020: #���˿ո�������ȫ�ǰ�ǵĹ�ʽΪ:���=ȫ��-0xfee0
            inside_code = 0x3000
        else:
            inside_code += 0xfee0
        rstring += unichr(inside_code)
    return rstring

if __name__ == '__main__':

    pass
