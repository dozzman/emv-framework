#!/usr/bin/python

from emv import *

emv = EMV()
res,sw1,sw3,tlv = emv.SELECT_AID([0xa0,0x00,0x00,0x00,0x03,0x10,0x10])
emv.log_print()
tlv.show()
