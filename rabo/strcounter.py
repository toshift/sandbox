# coding: utf-8
"""
入力された連続した文字をdictでカウントする
無い文字はカウントされないので比較時にtryする
"""
input_array = ["A","B","B","C","A"]
counter = {}
for status in input_array :
    if not status in counter:
        counter[status] = 1
    else:
        counter[status] += 1
try:
    if counter['A'] >= 2:
        print('OK')
    else:
        print('NG')
except:
    print('NG')
