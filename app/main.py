#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test(argv, options):
  # このコードは引数と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use arguments and outputs.
  # Edit and remove this code as you like.
  
  print argv
  list = []
  for i, v in enumerate(argv):
    str = v.encode('hex')
    str1 = str[:1]
    str2 = str[-1:]
    test = format(int(str1),'04b') + format(int(str2),'04b')
    list.append(format(int(str1),'04b') + format(int(str2),'04b'))
    rawstr = "".join(list)
  rawlist = [rawstr[i: i+6] for i in range(0, len(rawstr), 6)]
  print rawlist

  for raw in rawlist:
    print int(raw)
    print raw + "A"
      
test("1Aa","a")
