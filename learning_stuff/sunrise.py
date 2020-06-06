#!/usr/bin/python

import smbus
import time
from ctypes import c_short
from ctypes import c_byte
from ctypes import c_ubyte

DEVICE = 0x68  # Default device I2C address

bus = smbus.SMBus(1)  # Rev 2 Pi, Pi 2 & Pi 3 uses bus 1
# Rev 1 Pi uses bus 0
REG_CO2_DATA = 0x06


def main(addr=DEVICE):
    for i in range(0, 11):
        bus.write_byte_data(addr, 0x06, 0)
        data = bus.read_i2c_block_data(addr, 0x06, 2)
        print(data)
        sleep(1)


if __name__ == "__main__":
    main()
