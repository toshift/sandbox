#! /usr/bin/python
# -*- encoding: utf-8 -*-

import sys
try:
  import alsaaudio
except:
  print >> sys.stderr, "Error: pyalsaaudio not installed"
  sys.exit(1)


if len(sys.argv) < 3:
  print "USAGE: %s [name] [volume/ch1] ( [volume/ch2] )"
  sys.exit(1)

name = sys.argv[1]  # ミキサー項目名
vol = sys.argv[2:4] # 音量のパーセンテージ(0-100)の入ったリスト
# ミキサーオブジェクトの作成
try:
  print 'mixer = alsaaudio.Mixer("%s")' % name
  mixer = alsaaudio.Mixer(name)
except alsaaudio.ALSAAudioError:
  print >> sys.stderr, "Error: No such control: %s" % name
  sys.exit(1)

# (変更前の)音量をチャンネルごとにリストとして取得
# Masterは1ch
oldvol = mixer.getvolume()

# 音量を変更
# setvolume()で0から100以外の値を取ると例外alsaaudio.ALSAAudioErrorが発生
# alsaaudio.ALSAAudioError: Volume must be between 0 and 100
if len(vol) == 1:
  channel = alsaaudio.MIXER_CHANNEL_ALL
  print "mixer.setvolume(%d, alsaaudio.MIXER_CHANNEL_ALL)" % (int(vol[0]))
  mixer.setvolume(int(vol[0]), channel)
else:
  # 各チャンネルの音量を変更
  for i, v in enumerate(vol):
    mixer.setvolume(int(v), i)
    print "mixer.setvolume(%d, %d)" % (int(v), i)

# 変更前後の値を表示
print "%s: %s -> %s" % (name, oldvol, vol)