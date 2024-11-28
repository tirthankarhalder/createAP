#!/bin/bash
git clone https://github.com/aircrack-ng/rtl8812au.git
cd rtl8812au
make
sudo make install
find /lib/modules/`uname -r`/ -name "88XXau.ko"
