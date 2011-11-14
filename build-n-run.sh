#!/bin/sh
pyjsbuild $@ schoolbell
ln -sf schoolbell.html output/index.html
./schoolbelld.py
