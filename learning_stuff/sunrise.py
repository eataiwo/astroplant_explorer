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
sleep(1)

def main(addr=DEVICE):
    for i in range(0, 11):
        test = b'\x02\xBC'
        print(f'test is {test[0]} and {test[1]}')
        co2 = int.from_bytes(test, byteorder='big', signed=True)
        print(f'reference co2 is {co2}')
        bus.write_byte_data(addr, 0x06, 0)
        sleep(1/1000)
        data = bus.read_i2c_block_data(addr, 0x06, 2)
        co2_true = int.from_bytes(bytes(data), byteorder='big', signed=True)
        print(f' raw data is {data}')
        print(f' true co2 value is {co2_true}')
        #sleep(1)


if __name__ == "__main__":
    main()
