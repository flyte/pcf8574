PCF8574
=======

This is a Python library for use with the [PCF8574](http://www.nxp.com/documents/data_sheet/PCF8574.pdf) I2C IO expander chip. It abstracts the 8 bit IO port as a Python list, and allows the read/writing of individual pins or all ports at once.

## Installation

The library depends on the `smbus-cffi` package. You may need to `apt-get install libffi-dev` if you're on a debian based system. Otherwise, simply:

```
pip install pcf8574
```

## Usage

```python
In [1]: from pcf8574 import PCF8574

In [2]: i2c_port_num = 1

In [3]: pcf_address = 0x20

In [4]: pcf = PCF8574(i2c_port_num, pcf_address)

In [5]: pcf.port
Out[5]: [True, True, True, True, True, True, True, True]

In [6]: pcf.port[0] = False

In [7]: pcf.port
Out[7]: [False, True, True, True, True, True, True, True]

In [8]: pcf.port = [True, False, True, False, True, False, True, False]

In [9]: pcf.port
Out[9]: [True, False, True, False, True, False, True, False]

In [10]: pcf.port[7]
Out[10]: False

In [11]: pcf.port[6]
Out[11]: True
```