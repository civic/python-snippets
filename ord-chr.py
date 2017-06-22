#coding:utf8
import sys

print(sys.version)
if sys.version[0] == '2': # python2
    print("ascii code of 'a' = %d" % ord('a'))

    # python2ではunicode文字列リテラルはuが先頭につく
    print("unicode of u'あ' = %d " % ord(u'あ'))
    print("                   hex:%s " % hex(ord(u'あ')))
    print(u"u'\\u3042' == u'あ'     %s " % (u'\u3042' == u'あ'))

    # アスキーコードから文字へ
    print("chr(97) => %s" % chr(97)) #a
    print("unichr(0x3042) => %s" % unichr(0x3042)) #あ  unicode文字へはunichr関数で

if sys.version[0] == '3': # python3
    print("ascii code of 'a' = %d" % ord('a'))

    # python3ならunicode文字列でも扱いは変わらない
    print("unicode of 'あ' = %d " % ord('あ'))
    print("                   hex:%s " % hex(ord('あ')))
    print("'\\u3042' == 'あ'     %s " % ('\u3042' == 'あ'))

    # アスキーコードから文字へ
    print("chr(97) => %s" % chr(97)) #a
    print("chr(0x3042) => %s" % chr(0x3042))  #あ  python3ではunicode文字列も同じ扱いchrで
